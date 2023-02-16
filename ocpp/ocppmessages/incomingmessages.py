from dataclasses import dataclass, field

@dataclass
class BootNotificationResponsePayload:
    currentTime: str
    interval: int
    status: str = field(default = "Accepted")
