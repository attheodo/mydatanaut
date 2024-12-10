"""HTTP client module responsible for low-level HTTP communication with the MyData API."""

from typing import Dict, Optional

import requests

from .exceptions import (
    MyDataAuthenticationException,
    MyDataConnectionException,
    MyDataException,
    MyDataRateLimitExceededException,
)


class HttpClient:
    """A thin wrapper around `requests` providing convenient get/post methods and common headers.

    Attributes:
        session (requests.Session): A requests session object that maintains connection pooling and header state.
    """

    def __init__(
        self, headers: Dict[str, str], session: Optional[requests.Session] = None
    ):
        """Initialize the HttpClient.

        Args:
            headers (Dict[str, str]): Default headers to include in all requests.
            session (Optional[requests.Session], optional): A custom requests session. Defaults to None.
        """
        self.session = session or requests.Session()
        self.session.headers.update(headers)

    def post(self, url: str, data: str, timeout: int = 30) -> requests.Response:
        """Perform a POST request.

        Args:
            url (str): The request URL.
            data (str): The request payload (XML).
            timeout (int, optional): Request timeout in seconds. Defaults to 30.

        Returns:
            requests.Response: The HTTP response.

        Raises:
            MyDataHTTPException: If the response status code indicates an error.
        """
        try:
            response = self.session.post(url, data=data, timeout=timeout)
            self._raise_for_status(response, url)
            return response
        except requests.RequestException as exc:
            raise MyDataConnectionException(status_code=0, url=url, message=str(exc))

    def get(
        self, url: str, params: Optional[Dict[str, str]] = None, timeout: int = 30
    ) -> requests.Response:
        """Perform a GET request.

        Args:
            url (str): The request URL.
            params (Optional[Dict[str, str]]): URL query parameters. Defaults to None.
            timeout (int, optional): Request timeout in seconds. Defaults to 30.

        Returns:
            requests.Response: The HTTP response.

        Raises:
            MyDataHTTPException: If the response status code indicates an error.
        """
        try:
            response = self.session.get(url, params=params, timeout=timeout)
            self._raise_for_status(response, url)
            return response
        except requests.RequestException as exc:
            raise MyDataConnectionException(status_code=0, url=url, message=str(exc))

    @staticmethod
    def _raise_for_status(response: requests.Response, url: str):
        """Raise appropriate exceptions based on HTTP response status code."""
        status_code = response.status_code

        if status_code == 401 or status_code == 403:
            raise MyDataAuthenticationException(
                status_code,
                url,
                "Authentication failed. Please check your user id and subscription key.",
            )
        elif status_code == 429:
            raise MyDataRateLimitExceededException(status_code, url, response.text)
        elif status_code == 0:
            raise MyDataConnectionException(status_code, url, response.text)
        elif not response.ok:
            raise MyDataException(status_code, url, response.text)
