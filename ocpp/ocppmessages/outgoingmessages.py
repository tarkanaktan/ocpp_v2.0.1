from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class BootNotificationRequestPayload:
    charging_station: Dict
    reason: str

@dataclass
class HeartbeatRequestPayload:
    pass
