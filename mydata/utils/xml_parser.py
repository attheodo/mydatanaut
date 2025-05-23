import logging
from typing import Any, Type

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig


class XMLResponseParser:
    NAMESPACE_MAP = {
        None: "http://www.aade.gr/myDATA/invoice/v1.0",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "icls": "https://www.aade.gr/myDATA/incomeClassificaton/v1.0",
        "ecls": "https://www.aade.gr/myDATA/expensesClassificaton/v1.0",
    }

    def __init__(self):
        config = ParserConfig(fail_on_unknown_properties=False)
        self.parser = XmlParser(context=XmlContext(), config=config)

    def parse(self, xml_data: str, model: Type[Any]) -> Any:
        try:
            return self.parser.from_string(xml_data, model, ns_map=self.NAMESPACE_MAP)
        except Exception as e:
            logging.error(f"Error during XML parsing {e}", exc_info=True)
