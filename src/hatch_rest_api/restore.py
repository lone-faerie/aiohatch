import logging

from .util import (
    convert_to_percentage,
    safely_get_json_value,
    convert_from_percentage,
    convert_from_hex,
    convert_to_hex,
)
from .const import RIOT_FLAGS_CLOCK_ON, RIOT_FLAGS_CLOCK_24_HOUR, RestoreColor
from .shadow_client_subscriber import ShadowClientSubscriberMixin

_LOGGER = logging.getLogger(__name__)


class Restore(ShadowClientSubscriberMixin):
    audio_track: str = None
    firmware_version: str = None
    volume: int = 0

    is_online: bool = False
    current_playing: str = "none"
    routine_step: int = 0

    color: RestoreColor = None
    color_enabled: bool = False
    sound_id: int = 19998
    sound_enabled: bool = False
    brightness: int = 0
    clock: int = None
    flags: int = None

    def _update_local_state(self, state):
        _LOGGER.debug(f"update local state: {self.device_name}, {state}")
        if safely_get_json_value(state, "deviceInfo.f") is not None:
            self.firmware_version = safely_get_json_value(state, "deviceInfo.f")
        if safely_get_json_value(state, "connected") is not None:
            self.is_online = safely_get_json_value(state, "connected", bool)

        if safely_get_json_value(state, "content.playing") is not None:
            self.current_playing = safely_get_json_value(state, "content.playing")
        if safely_get_json_value(state, "sound.v") is not None:
            self.volume = convert_to_percentage(
                safely_get_json_value(state, "sound.v", int)
            )
        if safely_get_json_value(state, "sound.id", int) is not None:
            self.sound_id = safely_get_json_value(state, "sound.id", int)
        if safely_get_json_value(state, "sound.enabled", bool) is not None:
            self.sound_enabled = safely_get_json_value(state, "sound.enabled", bool)
        if safely_get_json_value(state, "color.id") is not None:
            self.color = RestoreColor(
                safely_get_json_value(state, "color.id", int)
            )
        if safely_get_json_value(state, "color.enabled", bool) is not None:
            self.color_enabled = safely_get_json_value(state, "color.enabled", bool)
        if safely_get_json_value(state, "color.i") is not None:
            self.brightness = convert_to_percentage(
                safely_get_json_value(state, "color.i", int)
            )
        if safely_get_json_value(state, "restoreClock.i") is not None:
            self.clock = convert_to_percentage(
                safely_get_json_value(state, "restoreClock.i", int)
            )
        if safely_get_json_value(state, "restoreClock.flags") is not None:
            self.flags = safely_get_json_value(state, "restoreClock.flags", int)

        if safely_get_json_value(state, "content.step", int) is not None:
            self.routine_step = safely_get_json_value(state, "content.step", int)

        _LOGGER.debug(f"new state:{self}")
        self.publish_updates()

    def __repr__(self):
        return {
            "device_name": self.device_name,
            "thing_name": self.thing_name,
            "mac": self.mac,
            "firmware_version": self.firmware_version,
            "is_on": self.is_on,
            "is_playing": self.is_playing,
            "volume": self.volume,
            "brightness": self.brightness,
            "document_version": self.document_version,
            "clock": self.clock,
            "flags": self.flags,
            "is_clock_on": self.is_clock_on,
            "is_clock_24h": self.is_clock_24h,
            "routine_step": self.routine_step
        }

    def __str__(self):
        return f"{self.__repr__()}"

    @property
    def is_on(self):
        return self.is_light_on or self.is_playing

    @property
    def is_light_on(self):
        return self.color_enabled

    @property
    def is_playing(self):
        return self.sound_enabled

    @property
    def is_clock_on(self):
        return self.flags is not None and self.flags & RIOT_FLAGS_CLOCK_ON

    @property
    def is_clock_24h(self):
        return self.flags is not None and self.flags & RIOT_FLAGS_CLOCK_24_HOUR

    def set_volume(self, percentage: int):
        _LOGGER.debug(f"Setting volume: {percentage}")
        self._update({"sound": {"v": convert_from_percentage(percentage)}})

    def set_clock(self, brightness: int = 0):
        _LOGGER.debug(f"Setting clock on: {brightness}")
        self._update(
            {"restoreClock": {"flags": self.flags | RIOT_FLAGS_CLOCK_ON, "i": convert_from_percentage(brightness)}}
        )

    def turn_clock_off(self):
        _LOGGER.debug(f"Turn off clock")
        self._update({"restoreClock": {"flags": self.flags ^ RIOT_FLAGS_CLOCK_ON, "i": 655}})

    def turn_off(self):
        _LOGGER.debug("Turning off sound")
        self._update({"content": {"routineId": 0, "step": 0, "playing": "none"}})

    def turn_light_off(self):
        _LOGGER.debug(f"Turning light off")
        # 9999 = custom color 9998 = turn off
        # if favorite is playing then light can be turned off without turning off sound
        if self.current_playing == "routine":
            self._update(
                {
                    "color": {
                        "enabled": false,
                    }
                }
            )
        if self.current_playing == "remote":
            self._update(
                {
                    "content": {
                        "playing": "none",
                    },
                    "color": {
                        "enabled": false,
                    },
                }
            )

    def set_color(
        self, color: RestoreColor, brightness: int = 0
    ):
        # 9999 = custom color 9998 = turn off
        new_color_id: int = color.value if (color is not RestoreColor.NONE) else self.color.value
        _LOGGER.debug(
            f"color: {color.name} brightness: {brightness}"
        )
        # If there is no sound playing, and you want to turn on the light the playing value has to be set to remote
        if self.current_playing == "none":
            self._update(
                {
                    "content": {
                        "routineId": 0,
                        "step": 0,
                        "playing": "remote",
                    },
                    "color": {
                        "id": new_color_id,
                        "i": convert_from_percentage(brightness),
                    },
                }
            )
        self._update(
            {
                "color": {
                    "id": new_color_id,
                    "i": convert_from_percentage(brightness),
                }
            }
        )

    def set_routine_step(self, step: int):
        pass
