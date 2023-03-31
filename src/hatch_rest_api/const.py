from enum import Enum

SENSITIVE_FIELD_NAMES = [
    "username",
    "password",
]

MAX_IOT_VALUE = 65535


class RestMiniAudioTrack(Enum):
    NONE = 0
    Heartbeat = 10124
    Water = 10125
    WhiteNoise = 10126
    Dryer = 10127
    Ocean = 10128
    Wind = 10129
    Rain = 10130
    Birds = 10131


class RestPlusAudioTrack(Enum):
    NONE = 0
    Stream = 2
    PinkNoise = 3
    Dryer = 4
    Ocean = 5
    Wind = 6
    Rain = 7
    Bird = 9
    Crickets = 10
    Brahms = 11
    Twinkle = 13
    RockABye = 14


REST_MINI_AUDIO_TRACKS = [
    RestMiniAudioTrack.NONE,
    RestMiniAudioTrack.WhiteNoise,
    RestMiniAudioTrack.Ocean,
    RestMiniAudioTrack.Rain,
    RestMiniAudioTrack.Water,
    RestMiniAudioTrack.Wind,
    RestMiniAudioTrack.Birds,
    RestMiniAudioTrack.Dryer,
    RestMiniAudioTrack.Heartbeat,
]


REST_PLUS_AUDIO_TRACKS = [
    RestPlusAudioTrack.NONE,
    RestPlusAudioTrack.Stream,
    RestPlusAudioTrack.PinkNoise,
    RestPlusAudioTrack.Dryer,
    RestPlusAudioTrack.Ocean,
    RestPlusAudioTrack.Wind,
    RestPlusAudioTrack.Rain,
    RestPlusAudioTrack.Bird,
    RestPlusAudioTrack.Crickets,
    RestPlusAudioTrack.Brahms,
    RestPlusAudioTrack.Twinkle,
    RestPlusAudioTrack.RockABye,
]

RIOT_FLAGS_CLOCK_24_HOUR = 2048
RIOT_FLAGS_CLOCK_ON = 32768

class RestoreColor(Enum):
    NONE = 0
    White = 1
    WarmWhite = 2
    Coral = 3
    Red = 4
    LightOrange = 5
    Peach = 6
    Orange = 7
    LightYellow = 8
    Yellow = 9
    Gold = 10

    def rgb_color(self):
        if self is RestoreColor.White:
            return 0, 0, 0
        elif self is RestoreColor.WarmWhite:
            return 0, 0, 0
        elif self is RestoreColor.Coral:
            return 0, 0, 0
        elif self is RestoreColor.Red:
            return 0, 0, 0
        elif self is RestoreColor.LightOrange:
            return 0, 0, 0
        elif self is RestoreColor.Peach:
            return 0, 0, 0
        elif self is RestoreColor.Orange:
            return 0, 0, 0
        elif self is RestoreColor.LightYellow:
            return 0, 0, 0
        elif self is RestoreColor.Yellow:
            return 0, 0, 0
        elif self is RestoreColor.Gold:
            return 0, 0, 0
        else:
            return -1, -1, -1
