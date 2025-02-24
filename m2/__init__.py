import copy
import sys

from mutwo.abjad_converters import *
from mutwo.abjad_parameters import *
from mutwo.abjad_utilities import *

from mutwo.common_generators import *
from mutwo.common_utilities import *

from mutwo.core_converters import *
from mutwo.core_events import *
from mutwo.core_parameters import *
from mutwo.core_utilities import *

from mutwo.csound_converters import *

from mutwo.ekmelily_converters import *

from mutwo.midi_converters import *

from mutwo.mmml_converters import *

from mutwo.music_converters import *
from mutwo.music_events import *
from mutwo.music_generators import *
from mutwo.music_parameters import *
from mutwo.music_utilities import *

from mutwo.reaper_converters import *

from mutwo.timeline_converters import *
from mutwo.timeline_interfaces import *
from mutwo.timeline_utilities import *

from .events import *
from .parameters import *

from .mmml import _mmml


# Add magic methods to module
class m2(sys.modules[__name__].__class__):
    def __matmul__(self, other):
        """Quickly convert between MMML expressions and mutwo events.

        **Example:**

        >>> import m2
        >>> e = m2 @ "n 1/4 c"
        >>> print(e)
        N(dur=R(1/4), ins=[], lyr=D(), pit=[WesternPitch('c', 4)], tag=None, tem=D(60.0), vol=W(-18.181818181818187))
        >>> m2 @ e
        'n 1/4 c4 mf _ _'
        """
        return _mmml(other, 0)

    def __add__(self, indentation: int):
        """Add indentation to converted mutwo event.

        This is useful for quickly embedding a mutwo event
        into an MMML expression.

        **Example:**

        >>> import m2
        >>> violin = m2.cns([m2.n("c", 1)], tag="viola")
        >>> mmml = f'''
        cnc music
            cns violin
                n 1/2 f4
                n 1/2 g4
            {(m2 + 1) @ violin}
        '''
        >>> print(mmml)
        cnc music
            cns violin
                n 1/2 f4
                n 1/2 g4
            cns viola
                n 1 c4 mf _ _
        """
        return _wrap(self, indentation)


class _wrap(object):
    def __init__(self, obj, indentation: int):
        self._m2 = obj
        self._mmml_indentation = indentation

    def __getattribute__(self, attr):
        if attr in ("_m2", "_mmml_indentation"):
            return super().__getattribute__(attr)
        return self._m2.__getattribute__(attr)

    def __matmul__(self, other):
        return _mmml(other, self._mmml_indentation)


sys.modules[__name__].__class__ = m2
del sys
