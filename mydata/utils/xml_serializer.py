from typing import Dict, Optional

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class XmlSerializerService:
    def __init__(self):
        config = SerializerConfig(indent="  ")
        self.serializer = XmlSerializer(context=XmlContext(), config=config)

    def serialize(self, obj: object, ns_map: Optional[Dict[str, str]] = None) -> str:
        return self.serializer.render(obj, ns_map=ns_map)
