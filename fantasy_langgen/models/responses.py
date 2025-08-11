from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import datetime


class VersionDiffItem(BaseModel):
    path: str
    operation: str  # "added", "removed", "modified"
    old_value: Optional[object]
    new_value: Optional[object]


class LanguageDiffResponse(BaseModel):
    base_version: int
    target_version: int
    changes: List[VersionDiffItem]
    affected_components: List[str]


class ForkResponse(BaseModel):
    new_language_id: str
    source_language: Dict[str, object]
    forked_at: datetime
    inherited_components: List[Dict[str, object]]
