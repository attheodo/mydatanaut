"""Configuration module for MyData Client environment and settings."""

from typing import Optional

import requests


class MyDataClientConfig:
    """Configuration class holding environment URLs and default settings for MyData API Client.

    Attributes:
        environment (str): The API environment ('production' or 'sandbox').
        is_provider (bool): Flag indicating whether the client is for provider API endpoints.
        timeout (int): Default timeout for requests in seconds.
        session (requests.Session): The requests session instance used by HTTP client.
    """

    DEV_ERP_URL = "https://mydataapidev.aade.gr/"
    PROD_ERP_URL = "https://mydatapi.aade.gr/myDATA/"

    DEV_PROVIDER_URL = "https://mydataapidev.aade.gr/myDataProvider/"
    PROD_PROVIDER_URL = "https://mydatapi.aade.gr/myDataProvider/"

    def __init__(
        self,
        environment: str = "production",
        is_provider: bool = False,
        timeout: int = 30,
        session: Optional[requests.Session] = None,
    ):
        """Initialize the MyDataClientConfig.

        Args:
            environment (str, optional): 'production' or 'sandbox'. Defaults to 'production'.
            is_provider (bool, optional): Whether to target provider URLs. Defaults to False.
            timeout (int, optional): Request timeout in seconds. Defaults to 30.
            session (Optional[requests.Session], optional): A custom requests session. Defaults to None.
        """
        self.environment = environment.lower()
        self.is_provider = is_provider
        self.timeout = timeout
        self.session = session or requests.Session()

    @property
    def is_sandbox(self) -> bool:
        """Check if the environment is sandbox."""
        return self.environment == "sandbox"

    @property
    def is_production(self) -> bool:
        """Check if the environment is production."""
        return self.environment == "production"

    @property
    def erp_url(self) -> str:
        """The ERP URL based on the selected environment."""
        return self.DEV_ERP_URL if self.is_sandbox else self.PROD_ERP_URL

    @property
    def provider_url(self) -> str:
        """The provider URL based on the selected environment."""
        return self.DEV_PROVIDER_URL if self.is_sandbox else self.PROD_PROVIDER_URL

    @property
    def base_url(self) -> str:
        """Base URL chosen depending on whether the client is a provider or ERP client."""
        return self.provider_url if self.is_provider else self.erp_url
