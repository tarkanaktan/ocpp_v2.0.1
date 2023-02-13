import json
import time
import uuid

from ocpp.exceptions import (
    FormatViolationError,
    NotImplementedError,
    OCPPError,
    PropertyConstraintViolationError,
    ProtocolError,
    TypeConstraintViolationError,
    UnknownCallErrorCodeError,
    ValidationError,
)

class MessageType:
    """Number identifying the different types of OCPP messages."""

    #: Call identifies a request.
    Call = 2

    #: CallResult identifies a successful response.
    CallResult = 3

    #: CallError identifies an erroneous response.
    CallError = 4


def unpack(msg):
    """
    Unpacks a message into either a Call, CallError or CallResult.
    """
    try:
        msg = json.loads(msg)
    except json.JSONDecodeError:
        raise FormatViolationError(
            details={"cause": "Message is not valid JSON", "ocpp_message": msg}
        )

    if not isinstance(msg, list):
        raise ProtocolError(
            details={
                "cause": (
                    "OCPP message hasn't the correct format. It "
                    f"should be a list, but got '{type(msg)}' "
                    "instead"
                )
            }
        )

    for cls in [Call, CallResult, CallError]:
        try:
            if msg[0] == cls.message_type_id:
                return cls(*msg[1:])
        except IndexError:
            raise ProtocolError(
                details={"cause": "Message does not contain MessageTypeId"}
            )
        except TypeError:
            raise ProtocolError(details={"cause": "Message is missing elements."})

    raise PropertyConstraintViolationError(
        details={"cause": f"MessageTypeId '{msg[0]}' isn't valid"}
    )

class Call:
    """A Call is a type of message that initiate a request/response sequence.
    Both central systems and charge points can send this message.

    From the specification:

        A Call always consists of 4 elements: The standard elements
        MessageTypeId and UniqueId, a specific Action that is required on the
        other side and a payload, the arguments to the Action. The syntax of a
        call looks like this:

            [<MessageTypeId>, "<UniqueId>", "<Action>", {<Payload>}]

        ...

        For example, a BootNotification request could look like this:

            [2,
             "19223201",
             "BootNotification",
             {
              "chargePointVendor": "VendorX",
              "chargePointModel": "SingleSocketCharger"
             }
            ]
    """

    message_type_id = 2

    def __init__(self, unique_id, action, payload):
        self.unique_id = unique_id
        self.action = action
        self.payload = payload

    def to_json(self):
        """Return a valid JSON representation of the instance."""
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.action,
                self.payload,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":")
        )

    def create_call_result(self, payload):
        call_result = CallResult(self.unique_id, payload)
        call_result.action = self.action
        return call_result

    def create_call_error(self, exception):
        error_code = "InternalError"
        error_description = "An unexpected error occurred."
        error_details = {}

        if isinstance(exception, OCPPError):
            error_code = exception.code
            error_description = exception.description
            error_details = exception.details

        return CallError(
            self.unique_id,
            error_code,
            error_description,
            error_details,
        )

    def __repr__(self):
        return (
            f"<Call - unique_id={self.unique_id}, action={self.action}, "
            f"payload={self.payload}>"
        )

class CallResult:
    """
    A CallResult is a message indicating that a Call has been handled
    successfully.

    From the specification:

        A CallResult always consists of 3 elements: The standard elements
        MessageTypeId, UniqueId and a payload, containing the response to the
        Action in the original Call. The syntax of a call looks like this:

            [<MessageTypeId>, "<UniqueId>", {<Payload>}]

        ...

        For example, a BootNotification response could look like this:

            [3,
             "19223201",
             {
              "status":"Accepted",
              "currentTime":"2013-02-01T20:53:32.486Z",
              "heartbeatInterval":300
             }
            ]

    """

    message_type_id = 3

    def __init__(self, unique_id, payload, action=None):
        self.unique_id = unique_id
        self.payload = payload

        # Strictly speaking no action is required in a CallResult. But in order
        # to validate the message it is needed.
        self.action = action

    def to_json(self):
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.payload,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":")
        )

    def __repr__(self):
        return (
            f"<CallResult - unique_id={self.unique_id}, "
            f"action={self.action}, "
            f"payload={self.payload}>"
        )

class CallError:
    """
    A CallError is a response to a Call that indicates an error.

    From the specification:

        CallError always consists of 5 elements: The standard elements
        MessageTypeId and UniqueId, an errorCode string, an errorDescription
        string and an errorDetails object.

        The syntax of a call looks like this:

            [<MessageTypeId>, "<UniqueId>", "<errorCode>", "<errorDescription>", {<errorDetails>}] # noqa
    """

    message_type_id = 4

    def __init__(self, unique_id, error_code, error_description, error_details=None):
        self.unique_id = unique_id
        self.error_code = error_code
        self.error_description = error_description
        self.error_details = error_details

    def to_json(self):
        return json.dumps(
            [
                self.message_type_id,
                self.unique_id,
                self.error_code,
                self.error_description,
                self.error_details,
            ],
            # By default json.dumps() adds a white space after every separator.
            # By setting the separator manually that can be avoided.
            separators=(",", ":")
        )

    def to_exception(self):
        """Return the exception that corresponds to the CallError."""
        for error in OCPPError.__subclasses__():
            if error.code == self.error_code:
                return error(
                    description=self.error_description, details=self.error_details
                )

        raise UnknownCallErrorCodeError(
            "Error code '%s' is not defined by the" " OCPP specification",
            self.error_code,
        )

    def __repr__(self):
        return (
            f"<CallError - unique_id={self.unique_id}, "
            f"error_code={self.error_code}, "
            f"error_description={self.error_description}, "
            f"error_details={self.error_details}>"
        )