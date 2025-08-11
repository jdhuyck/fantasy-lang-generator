from typing import List
from pydantic import BaseModel, Field, field_validator, model_validator


class CulturalInfluences(BaseModel):
    environment: str
    technology_level: int
    social_structure: str = Field(
        default="tribal",
        pattern="^(clan_hierarchy|egalitarian|matriarchal|imperial|tribal)$"
    )
    values: List[str] = Field(default_factory=list)
    taboos: List[str] = Field(default_factory=list)
    contact_languages: List[str] = Field(default_factory=list)

    @field_validator("technology_level")
    def validate_tech_level(cls, v):
        if not 1 <= v <= 10:
            raise ValueError("Technology level must be between 1-10")
        return v
    
    @field_validator("environment")
    def validate_environment(cls, v):
        valid_envs = ["mountainous", "forest", "desert", "coastal", "urban", "underground"]
        if v not in valid_envs:
            raise ValueError(f"Invalid environment. Must be one of: {valid_envs}")
        return v
