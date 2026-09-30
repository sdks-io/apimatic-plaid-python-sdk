from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class State(str, Enum):
    """The state, or status, of the deposit switch.

    - ``initialized`` – The deposit switch has been initialized with the user entering the information required to
        submit the deposit switch request.

    - ``processing`` – The deposit switch request has been submitted and is being processed.

    - ``completed`` – The user's employer has fulfilled the deposit switch request.

    - ``error`` – There was an error processing the deposit switch request."""

    INITIALIZED = "initialized"
    PROCESSING = "processing"
    COMPLETED = "completed"
    ERROR = "error"

    __str__ = str.__str__


StateOrStr: TypeAlias = Annotated[State | str, open_enum_validator(State)]
