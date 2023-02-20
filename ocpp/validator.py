from messagetypes import MessageType
from typing import Callable, Dict, Union
from messagetypes import Call,CallResult
from exceptions import ValidationError, NotImplementedError
from jsonschema.exceptions import ValidationError as SchemaValidationError

from jsonschema import Draft4Validator
import os
import json

_validators: Dict[str, Draft4Validator] = {}

def get_validator(
    message_type_id: int, action: str, parse_float: Callable = float
) -> Dict[str,Draft4Validator]:
    """
    Read schema from disk and return as `Draft4Validator`. Instances will be
    cached for performance reasons.
    """
    schema_name = action
    if message_type_id == MessageType.CallResult:
        schema_name += "Response"
    elif message_type_id == MessageType.Call:
        schema_name += "Request"

    if schema_name in _validators:
        return _validators[schema_name]

    dir, _ = os.path.split(os.path.realpath(__file__))
    relative_path = f"schemas/{schema_name}.json"
    path = os.path.join(dir, relative_path)

    with open(path, "r", encoding="utf-8-sig") as f:
        data = f.read()
        validator = Draft4Validator(json.loads(data, parse_float=parse_float))
        _validators[schema_name] = validator

    return _validators[schema_name]

def validatePayload(message: Union[Call,CallResult]):
    print(f"validation of {message}")
    if(type(message) not in [Call,CallResult]):
        raise ValidationError(
            f"It's '{type(message)}', but it should "
            "be either 'Call'  or 'CallResult'."
        )
    try:
        validator = get_validator(message_type_id=message.message_type_id,action=message.action)
    except:
        raise NotImplementedError(
            details={"cause": f"Failed to validate action: {message.action}"}
        )
    try:
        validator.validate(message.payload)
    except SchemaValidationError as e:
        print(e)
