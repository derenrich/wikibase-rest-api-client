from typing import Any, Dict, Optional


class GettableModel:
    """Helper for models so that we can get a value from a dict without crashing"""

    additional_properties: Dict[str, Any]

    def get(self, key: str) -> Optional[Any]:
        return self.additional_properties.get(key, None)
