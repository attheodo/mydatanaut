"""Custom exception classes for MyData client operations."""


class MyDataException(Exception):
    """Base exception for all MyData-related errors."""

    pass


class MyDataHTTPException(MyDataException):
    """Base exception for HTTP-related errors when communicating with the MyData API."""

    def __init__(self, status_code: int, url: str, message: str = ""):
        self.status_code = status_code
        self.url = url
        self.message = message
        super().__init__(f"HTTP[{status_code}] {url}: {message}")


class MyDataXMLParseException(MyDataException):
    """Exception raised for errors encountered during XML parsing."""

    def __init__(self, original_exception: Exception):
        self.original_exception = original_exception
        super().__init__(f"Failed to parse XML data: {original_exception}")


class MyDataInvalidResponseException(MyDataHTTPException):
    """Exception raised when the response from the server is empty or invalid."""

    def __init__(
        self,
        url: str,
        message: str = "Empty or invalid response received from AADE MyData API",
    ):
        super().__init__(status_code=200, url=url, message=message)


class MyDataAuthenticationException(MyDataHTTPException):
    """Exception raised for authentication failures (e.g., HTTP 401)."""

    pass


class MyDataConnectionException(MyDataHTTPException):
    """Exception raised for connection-related errors (HTTP code 0 or similar)."""

    pass


class MyDataRateLimitExceededException(MyDataHTTPException):
    """Exception raised when rate limit is exceeded (HTTP 429)."""

    pass


class MyDataDataException(MyDataHTTPException):
    """Generic data or transmission error exception for unexpected HTTP errors."""

    pass
