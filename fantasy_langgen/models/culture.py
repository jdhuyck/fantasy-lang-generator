from typing import List
from pydantic import BaseModel, conint, Field


class CulturalInfluence(BaseModel):
    environment: str = Field(
        default="forest",
        regex="^(mountainous|forest|desert|coastal|urban|underground)$"
    )
    technology_level: conint(ge=1, le=10) = 3
    social_structure: str = Field(
        default="tribal",
        regex="^(clan_hierarchy|egalitarian|matriarchal|imperial|tribal)$"
    )
    values: List[str] = Field(default_factory=list)
    taboos: List[str] = Field(default_factory=list)
    contact_languages: List[str] = Field(default_factory=list)
