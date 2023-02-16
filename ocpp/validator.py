from messagetypes import MessageType
from typing import Callable, Dict

from jsonschema import Draft4Validator
import os
import json

_validators: Dict[str, Draft4Validator] = {}

def get_validator(
    message_type_id: int, action: str, ocpp_version: str, parse_float: Callable = float
) -> Draft4Validator:
    """
    Read schema from disk and return as `Draft4Validator`. Instances will be
    cached for performance reasons.
    """
    schema_name = action
    if message_type_id == MessageType.CallResult:
        schema_name += "Response"
    elif message_type_id == MessageType.Call:
        schema_name += "Request"

    cache_key = schema_name + "_" + ocpp_version
    if cache_key in _validators:
        return _validators[cache_key]

    dir, _ = os.path.split(os.path.realpath(__file__))
    relative_path = f"schemas/{schema_name}.json"
    path = os.path.join(dir, relative_path)

    with open(path, "r", encoding="utf-8-sig") as f:
        data = f.read()
        validator = Draft4Validator(json.loads(data, parse_float=parse_float))
        _validators[cache_key] = validator

    return _validators[cache_key]