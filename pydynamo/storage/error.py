from enum import Enum


class ErrorType(Enum):
    NOT_FOUND = 0
    INVALID_INPUT = 1


class StorageException(Exception):
    def __init__(self, error_type: ErrorType, msg: str) -> None:
        self.error_type = error_type
        self.msg = msg

class NotFoundError(StorageException):
    pass