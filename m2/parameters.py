from mutwo import core_parameters
from mutwo import music_parameters

__all__ = (
    "duration",
    "tempo",
    "pitch",
    "pitch_list",
    "volume",
    "lyric",
    "pitch_interval",
)

duration = core_parameters.abc.Duration.from_any
tempo = core_parameters.abc.Tempo.from_any
pitch = music_parameters.abc.Pitch.from_any
pitch_list = music_parameters.abc.PitchList.from_any
volume = music_parameters.abc.Volume.from_any
lyric = music_parameters.abc.Lyric.from_any
pitch_interval = music_parameters.abc.PitchInterval.from_any
