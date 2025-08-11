from pydantic import BaseModel, field_validator, model_validator


class GeneratedWord(BaseModel):
    word: str
    meaning: str
    components: list[str]
    confidence: float

    @field_validator("confidence")
    def validate_confidence(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Confidence must be between 0-1")
        return v

class DerivedContent(BaseModel):
    generated_words: list[GeneratedWord]
    sample_sentences: list[dict]
    generation_parameters: dict

    @model_validator(mode="after")
    def validate_generated_content(self):
        for word in self.generated_words:
            if word.confidence < 0.5 and "unverified" not in self.generation_parameters.get("tags", []):
                raise ValueError("Low-confidence words must be tagged as unverified")
        return self