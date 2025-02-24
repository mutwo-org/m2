import typing

from mutwo import core_events
from mutwo import mmml_converters


def _mmml(o: typing.Any, indentation: int) -> core_events.abc.Event | str:
    match o:
        case str():
            return _mmml2e(o)
        case core_events.abc.Event():
            mmml = _e2mmml(o)
            if indentation:
                i = mmml_converters.constants.INDENTATION * indentation
                indented = f"\n{i}".join(mmml.splitlines())
                mmml = "\n".join(
                    # Drop empty lines with only white-space
                    [e if e.strip() else "" for e in indented.splitlines()]
                )
            return mmml
        case _:
            raise TypeError(f"Can't convert {o} to str or event")


_mmml2e = mmml_converters.MMMLExpressionToEvent()
_e2mmml = mmml_converters.EventToMMMLExpression()
