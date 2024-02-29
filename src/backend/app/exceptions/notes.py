from enum import Enum

from app.exceptions import base as app_exceptions


class NoteExceptionInfo(app_exceptions.ExceptionEnum, Enum):
    NOTE_ALREADY_EXISTS = "4000", "Note already exists"
    NOTE_NOT_FOUND = "4001", "Note not found"
    NOTE_FORBIDDEN = "4003", "Access Denied"


class NoteException(app_exceptions.BaseAppException):
    """user exception"""

    class NoteExistsException(app_exceptions.BaseConflictException):
        code: str = NoteExceptionInfo.NOTE_ALREADY_EXISTS.code
        error: str = NoteExceptionInfo.NOTE_ALREADY_EXISTS.error

    class NoteNotFoundException(app_exceptions.BaseNotFoundException):
        code: str = NoteExceptionInfo.NOTE_NOT_FOUND.code
        error: str = NoteExceptionInfo.NOTE_NOT_FOUND.error

    class NoteForbiddenException(app_exceptions.BaseForbiddenException):
        code: str = NoteExceptionInfo.NOTE_FORBIDDEN.code
        error: str = NoteExceptionInfo.NOTE_FORBIDDEN.error
