from werkzeug.routing import BaseConverter
from typing import List


class ListConverter(BaseConverter):
    """
    Converter for list path variables.
    This converter supports conversion of urls like /names/Tesla,Einstein,Hawking
    """

    # Separator character that separates each element in the list
    SEPARATOR = ','
    # Name of the converter. This name should be used when registering the converter
    NAME = 'list'

    def to_python(self, value: str) -> List[str]:
        return value.split(ListConverter.SEPARATOR)

    def to_url(self, values: List[str]) -> str:
        return ListConverter.SEPARATOR.join(values)