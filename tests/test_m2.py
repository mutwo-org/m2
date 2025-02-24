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
