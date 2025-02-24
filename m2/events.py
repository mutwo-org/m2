"""Event abbreviations"""

from mutwo import core_events
from mutwo import music_events

__all__ = ("cns", "cnc", "chn", "n")

cns = core_events.Consecution
cnc = core_events.Concurrence
chn = core_events.Chronon
n = music_events.NoteLike
