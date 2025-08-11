from datetime import datetime, timezone
from typing import Optional, List, Dict
from pydantic import BaseModel, Field
from .phonology import Phonology
from .vocabulary import Vocabulary
from .grammar import Grammar
from .culture import CulturalInfluences


class VersionHistory(BaseModel):
    version: int = Field(..., gt=0)
    modified_at: datetime
    modified_by: str
    changeset: Optional[str] = None


class LanguageMetadata(BaseModel):
    language_name: str = Field(..., min_length=1, max_length=50)
    creator: str
    created_at: datetime = Field(default_factory=datetime.now(tz=timezone.utc))  # noqa:E501
    last_modified: datetime = Field(default_factory=datetime.now(tz=timezone.utc))  # noqa:E501
    version: int = Field(default=1, gt=0)
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

    # Versioning fields
    parent_id: Optional[str] = None
    original_creator: Optional[str] = None
    version_history: List[VersionHistory] = Field(default_factory=list)

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class DerivedContent(BaseModel):
    generated_words: List[Dict[str, object]] = Field(default_factory=list)
    sample_sentence: List[Dict[str, str]] = Field(default_factory=list)
    generation_parameters: Dict[str, object]


class Language(BaseModel):
    metadata: LanguageMetadata
    phonology: Phonology
    vocabulary: Vocabulary
    grammar: Grammar
    cultural_influences: CulturalInfluences
    derived_content: DerivedContent = Field(default_factory=DerivedContent)
