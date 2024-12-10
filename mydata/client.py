"""Main client class for interacting with the AADE/myData API."""

from typing import Any, Dict, List, Optional, Type

from .client_config import MyDataClientConfig
from .exceptions import MyDataXMLParseException
from .http_client import HttpClient
from .models.generated.requested_doc import RequestedDoc
from .models.generated.response_doc import ResponseDoc
from .models.invoice import Invoice
from .models.invoices_document import InvoicesDocument
from .utils.xml_parser import XMLResponseParser
from .utils.xml_serializer import XmlSerializerService


class MyDataClient:
    """Client class for interacting with AADE/myData API endpoints.

    Provides methods to send invoices and request documents. Serializes requests
    to XML and deserializes responses to Python objects.
    """

    def __init__(
        self,
        user_id: str,
        subscription_key: str,
        config: Optional[MyDataClientConfig] = None,
        http_client: Optional[HttpClient] = None,
        serializer: Optional[XmlSerializerService] = None,
        deserializer: Optional[XMLResponseParser] = None,
    ):
        """Initialize the MyDataClient.

        Args:
            user_id (str): The AADE user ID.
            subscription_key (str): The subscription key provided by AADE.
            config (Optional[MyDataClientConfig], optional): Configuration object. Defaults to None.
            http_client (Optional[HttpClient], optional): A pre-configured HttpClient. Defaults to None.
            serializer (Optional[XmlSerializerService], optional): XML serializer. Defaults to None.
            deserializer (Optional[XMLResponseParser], optional): XML response parser. Defaults to None.
        """
        self.user_id = user_id
        self.subscription_key = subscription_key
        self.config = config or MyDataClientConfig()
        self.serializer = serializer or XmlSerializerService()
        self.deserializer = deserializer or XMLResponseParser()

        self.http_client = http_client or HttpClient(
            headers=self._default_headers(), session=self.config.session
        )

    def _default_headers(self) -> dict:
        """Default headers for all API requests."""
        return {
            "aade-user-id": self.user_id,
            "ocp-apim-subscription-key": self.subscription_key,
            "Content-Type": "text/xml",
        }

    def _get(self, endpoint: str, params: Dict[str, str] = None) -> str:
        """Helper method to perform GET requests.

        Args:
            endpoint (str): The endpoint path (relative to base_url).
            params (Dict[str, str], optional): URL query parameters. Defaults to None.

        Returns:
            str: The response text.

        Raises:
            MyDataHTTPException: If an HTTP error occurs.
        """
        url = f"{self.config.base_url}{endpoint}"
        response = self.http_client.get(url, params=params, timeout=self.config.timeout)
        return response.text

    def _post(self, endpoint: str, data: str) -> str:
        """Helper method to perform POST requests.

        Args:
            endpoint (str): The endpoint path (relative to base_url).
            data (str): The XML payload.

        Returns:
            str: The response text.

        Raises:
            MyDataHTTPException: If an HTTP error occurs.
        """
        url = f"{self.config.base_url}{endpoint}"
        response = self.http_client.post(url, data=data, timeout=self.config.timeout)
        return response.text

    def _parse_response(self, xml_data: str, model: Type[Any]) -> Any:
        """Parse XML response data into the specified model.

        Args:
            xml_data (str): The raw XML response.
            model (Type[Any]): The model class to deserialize into.

        Returns:
            Any: An instance of the model populated with parsed data.

        Raises:
            MyDataXMLParseException: If XML parsing fails.
        """
        try:
            return self.deserializer.parse(xml_data, model)
        except Exception as e:
            raise MyDataXMLParseException(e)

    def send_invoice(
        self, invoice: Invoice, response_model: Type[Any] = ResponseDoc
    ) -> ResponseDoc:
        """Send a single invoice to AADE/myData.

        Args:
            invoice (Invoice): The invoice object to be sent.
            response_model (Type[Any], optional): The model to parse the response into. Defaults to ResponseDoc.

        Returns:
            Any: Parsed response object.
        """
        return self.send_invoices([invoice], response_model=response_model)

    def send_invoices(
        self,
        invoices: List[Invoice],
        response_model: Type[Any] = ResponseDoc,
    ) -> ResponseDoc:
        """Send multiple invoices to AADE/myData.

        Args:
            invoices (List[Invoice]): A list of Invoice objects.
            response_model (Type[Any], optional): The model to parse the response into. Defaults to ResponseDoc.

        Returns:
            ResponseDoc: Parsed response object.
        """
        doc = InvoicesDocument(invoices=invoices, serializer=self.serializer)
        xml_data = doc.as_xml()
        response = self._post("SendInvoices", xml_data)
        return self._parse_response(response, response_model)

    def request_transmitted_docs(
        self,
        mark: int = 0,
        response_model: Type[Any] = RequestedDoc,
    ) -> RequestedDoc:
        """Request transmitted documents from AADE/myData by mark The API will return all documents with mark greater
        than or equal to the provided mark.

        Args:
            mark (int): The unique document mark.
            response_model (Type[Any], optional): The model to parse the response into. Defaults to RequestedDoc.

        Returns:
            RequestedDoc: Parsed requested document model.
        """
        response = self._get("RequestTransmittedDocs", params={"mark": str(mark)})
        return self._parse_response(response, response_model)

    def cancel_invoice(self, mark: int, response_model: Type[Any] = ResponseDoc):
        """Cancels an invoice by its mark

        Args:
            mark (int): The unique document mark to be canceled

        Returns:
            ResponseDoc: Parsed response object.
        """
        response = self._post(f"CancelInvoice?mark={mark}", None)
        return self._parse_response(response, response_model)
