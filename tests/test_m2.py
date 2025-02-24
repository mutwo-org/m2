from mutwo import mmml_converters

import m2


def test_m2_libraries():
    """Primitive test which ensures all supported libraries are imported"""

    # mutwo.abjad
    assert m2.ConsecutionToAbjadVoice
    # mutwo.core
    assert m2.Consecution
    # mutwo.common
    assert m2.ActivityLevel
    # mutwo.csound
    assert m2.EventToCsoundScore
    # mutwo.ekmelily
    assert m2.EkmelilyTuningFileConverter
    # mutwo.midi
    assert m2.EventToMidiFile
    # mutwo.mmml
    assert m2.MMMLExpressionToEvent
    # mutwo.music
    assert m2.NoteLike
    # mutwo.reaper
    assert m2.EventToReaperMarkerString
    # mutwo.timeline
    assert m2.EventPlacement


def test_event_abbreviations():
    """Ensure stability of API"""

    assert m2.cns == m2.Consecution
    assert m2.cnc == m2.Concurrence
    assert m2.chn == m2.Chronon
    assert m2.n == m2.NoteLike


def test_mmml_conversion():
    """Verify magic MMML conversion API works ok"""

    n = m2.n("f", 1, "mp")
    n_mmml = "n 1 f4 mp _ _"

    # MMML => Event
    assert m2 @ n_mmml == n
    # Event => MMML
    assert m2 @ n == n_mmml

    # Test indentation
    cns = m2.cns([n, n])
    cns_mmml = r"""cns

    n 1 f4 mp _ _
    n 1 f4 mp _ _
"""

    cns_mmml_indent_1 = r"""cns

        n 1 f4 mp _ _
        n 1 f4 mp _ _"""

    assert (m2 + 1) @ cns == cns_mmml_indent_1

    # Ensure indentation doesn't persist
    assert m2 @ cns == cns_mmml
