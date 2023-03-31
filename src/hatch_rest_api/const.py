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
    LightGreen = 11
    Mint = 12
    Green = 13
    LightTurquoise = 14
    Aqua = 15
    Turquoise = 15
    LightBlue = 16
    Sky = 17
    Blue = 18
    Lilac = 19
    Purple = 20
    LightPink = 21

    def rgb(self):
        if self is RestoreColor.White:
            return 255, 255, 255
        elif self is RestoreColor.WarmWhite:
            return 253, 245, 230
        elif self is RestoreColor.Coral:
            return 255, 228, 225
        elif self is RestoreColor.Red:
            return 255, 0, 0
        elif self is RestoreColor.LightOrange:
            return 255, 218, 185

RESTORE_COLORS = [
    RestoreColor.NONE,
    RestoreColor.White,
    RestoreColor.WarmWhite,
    RestoreColor.Coral,
    RestoreColor.Red,
    RestoreColor.LightOrange,
    RestoreColor.Peach,
    RestoreColor.Orange,
    RestoreColor.LightYellow,
    RestoreColor.Yellow,
    RestoreColor.Gold,
    RestoreColor.LightGreen,
    RestoreColor.Mint,
    RestoreColor.Green,
    RestoreColor.LightTurquoise,
    RestoreColor.Aqua,
    RestoreColor.Turquoise,
    RestoreColor.LightBlue,
    RestoreColor.Sky,
    RestoreColor.Blue,
    RestoreColor.Lilac,
    RestoreColor.Purple,
    RestoreColor.LightPink,
]
