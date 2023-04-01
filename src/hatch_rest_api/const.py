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
    MalibuSunrise = 20
    PortlandLighthouse = 
    White = 229
    WarmWhite = 228
    Coral = 205
    Red = 206
    LightOrange = 207
    Peach = 208
    Orange = 209
    LightYellow = 210
    Yellow = 211
    Gold = 212
    LightGreen = 213
    Mint = 214
    Green = 215
    LightTurquoise = 225
    Aqua = 226
    Turquoise = 227
    LightBlue = 216
    Sky = 217
    Blue = 218
    Lilac = 220
    Purple = 221
    LightPink = 222

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
