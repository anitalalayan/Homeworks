from fastapi import HTTPException, status

class ValidationError(HTTPException):
    """Custom exception for validation-related errors."""
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

class FileError(HTTPException):
    """Custom exception for file-related errors."""
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=message)

class NotFoundError(HTTPException):
    """Custom exception for not-found errors."""
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)