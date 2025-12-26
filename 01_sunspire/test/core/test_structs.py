from dataclasses import dataclass, field
from typing import Any, List, Dict, Optional

@dataclass
class AttackResult:
    """
    Standardized result object for all attack/test actions.
    """
    success: bool
    message: str
    data: Any = None
    artifacts: List[str] = field(default_factory=list)