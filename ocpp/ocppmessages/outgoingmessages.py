from dataclasses import dataclass,field
from typing import Dict, List, Optional


@dataclass
class BootNotificationRequestPayload:
    charging_station: Dict
    reason: str = field(default = "PowerUp")

@dataclass
class HeartbeatRequestPayload:
    pass
