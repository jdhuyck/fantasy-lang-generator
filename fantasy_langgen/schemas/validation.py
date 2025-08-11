import json
from pathlib import Path
from jsonschema import validate
from typing import Dict, Any


def load_schema() -> Dict[str, Any]:
    schema_path = Path(__file__).parent / "language_schema.json"
    with open(schema_path) as f:
        return json.load(f)


def validate_language(data: Dict[str, Any]) -> None:
    schema = load_schema()
    validate(instance=data, schema=schema)
