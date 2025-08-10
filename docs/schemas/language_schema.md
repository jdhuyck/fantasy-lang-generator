# Formal JSON Schema

```json
{
    "$schema": "https://json-schema.org/draft-07/schema#",
    "title": "Fantasy Language",
    "type": "object",
    "properties": {
        "metadata": { "$ref": "#/definitions/metadata" },
        "phonology": { "$ref": "#/definitions/phonology" },
        "vocabulary": { "$ref": "#/definitions/vocabulary" },
        "grammar": { "$ref": "#/definitions/grammar" },
        "cultural_influences": { "$ref": "#/definitions/cultural_influences" }
    },
    "required": ["metadata", "phonology"],
    "definitions": {
        "metadata": {
            "type": "object",
            "properties": {
                "language_name": {
                    "type": "string",
                    "min_length": 1,
                    "description": "Primary name of the language"
                },
                "creator": {
                    "type": "string",
                    "description": "Author/creator of the language"
                },
                "created_at": {
                    "type": "string",
                    "format": "date-time",
                    "description": "ISO8601 creation timestamp"
                },
                "last_modified": {
                    "type": "string",
                    "format": "date-time",
                    "description": "ISO8601 last modified timestamp"
                },
                "version": {
                    "type": "number",
                    "minimum": 0,
                    "description": "Version number of the language definition"
                },
                "description": {
                    "type": "string",
                    "description": "Optional description of the language"
                },
                "tags": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "Categorization tags for the language"
                }
            },
            "required": ["language_name", "creator", "created_at"],
            "additionalProperties": false
        },

        "phonology": {
            "type": "object",
            "properties": {
                "consonants": {
                    "type": "object",
                    "properties": {
                        "stops": {
                            "type": "array",
                            "items" : { "type": "string", "maxLength": 2 },
                            "description": "Plosive consonant sounds"
                        },
                        "fricatives": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 2 },
                            "description": "Fricative consonant sounds"
                        },
                        "nasals": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 2 },
                            "description": "Nasal consonant sounds"
                        },
                        "liquids": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 2 },
                            "descriptions": "Liquid/glide consonant sounds"
                        },
                        "constraints": {
                            "type": "object",
                            "properties": {
                                "initial_clusters": {
                                    "type": "array",
                                    "items": { "type": "string", "maxLength": 3 },
                                    "description": "Allowed initial consonant clusters"
                                },
                                "forbidden_clusters": {
                                    "type": "array",
                                    "items": { "type": "string", "maxLength": 3 },
                                    "description": "Prohibited consonant clusters"
                                }
                            },
                            "additionalProperties": false
                        }
                    },
                    "required": ["stops", "fricatives"],
                    "additionalProperties": false
                },
                "vowels": {
                    "type": "object",
                    "properties": {
                        "short": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 1 },
                            "description": "Short vowel sounds"
                        },
                        "long": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 2 },
                            "description": "Long vowel sounds"
                        },
                        "diphthongs": {
                            "type": "array",
                            "items": { "type": "string", "maxLength": 2 },
                            "description": "Diphthong combinations"
                        }
                    },
                    "required": ["short"],
                    "additionalProperties": false
                },
                "syllable": {
                    "type": "object",
                    "properties": {
                        "structure": {
                            "type": "string",
                            "pattern": "[CV()]+$",
                            "description": "Syllable structure pattern using C/V notation"
                        },
                        "stress_pattern": {
                            "type": "string",
                            "enum": ["initial", "penultimate", "ultimate", "none"],
                            "description": "Primary stress position in words"
                        }
                    },
                    "required": ["structure"],
                    "additionalProperties": false
                }
                "phonotactics": {
                    "type": "object",
                    "properties": {
                        "max_initial_consonants": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Maximum consonants at word start"
                        },
                        "max_final_consonants": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Maximum consonants at word end"
                        },
                        "vowel_harmony": {
                            "type": "boolean",
                            "description": "Whether vowel harmony rules apply"
                        }
                    },
                    "additionalProperties": false
                }
            },
            "required": ["consonants", "vowels", "syllable"]
        },

        "vocabluary": {
            "type": "object",
            "properties": {
                "base_words": {
                    "type": "object",
                    "additionalProperties": { "type": "string" },
                    "description": "Dictionary of base words and their meanings"
                },
                "word_formation_rules": {
                    "type": "object",
                    "properties": {
                        "diminutive": {
                            "type": "string",
                            "description": "Suffix for diminutive forms"
                        },
                        "augmentative": {
                            "type": "string",
                            "description": "Suffix for augmentative forms"
                        },
                        "material": {
                            "type": "string",
                            "description": "Suffix indicating material compositions"
                        }
                    },
                    "additionalProperties": false
                },
                "semantic_fields": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "object",
                        "additionalProperties": { "type": "string" }
                    },
                    "description": "Words organized by conceptual categories"
                }
            },
            "additionalProperties": false
        },

        "grammar": {
            "type": "object",
            "properties": {
                "word_order": {
                    "type": "string",
                    "enum": ["SOV", "SVO", "VSO", "VOS", "OVS", "OSV"],
                    "description": "Default sentence word order"
                },
                "noun": {
                    "type": "object",
                    "properties": {
                        "cases": {
                            "type": "array",
                            "items": { "type": "string" },
                            "description": "Grammatical cases in the language"
                        },
                        "genders": {
                            "type": "array",
                            "items": { "type": "string" },
                            "description": "Noun gender categories"
                        },
                        "plural_forms": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "pattern": { "type": "string" },
                                    "suffix": { "type": "string" },
                                    "exceptions": {
                                        "type": "object",
                                        "additionalProperties": { "type": "string" }
                                    }
                                },
                                "required": ["pattern"]
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "verb": {
                    "type": "object",
                    "properties": {
                        "tenses": {
                            "type": "array",
                            "items": { "type": "string" },
                            "description": "Verb tense system"
                        },
                        "conjugation_patterns": {
                            "type": "object",
                            "additionalProperties": {
                                "type": "object",
                                "additionalProperties": { "type": "string" }
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "adjectives": {
                    "type": "object",
                    "properties": {
                        "position": {
                            "type": "string",
                            "enum": ["prenominal", "postnomial"],
                            "description": "Default adjective position"
                        },
                        "comparative": { "type": "string" },
                        "superlative": { "type": "string" }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },

        "cultural_influences": {
            "type": "object",
            "properties": {
                "environment": {
                    "type": "string",
                    "enum": ["mountainous", "forest", "desert", "coastal", "urban", "underground"],
                    "description": "Primary environment of the culture"
                },
                "technology_level": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Technological sophistication (1-10 scale)"
                },
                "social_structure": {
                    "type": "string",
                    "enum": ["clan_hierarchy", "egalitarian", "matriarchal", "imperial", "tribal"],
                    "description": "Organization of society"
                },
                "values": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "Core cultural values"
                },
                "taboos": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "Forbidden concepts/actions"
                },
                "contact_languages": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "Languages this culture interacts with"
                }
            },
            "additionalProperties": false
        },

        "derived_content": {
            "type": "object",
            "properties": {
                "generated_words": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "word": { "type": "string" },
                            "meaning": { "type": "string" },
                            "components": {
                                "type": "array",
                                "items": { "type": "string" }
                            },
                            "confidence": {
                                "type": "number",
                                "minimum": 0,
                                "maximum": 1
                            }
                        },
                        "required": ["word", "meaning"]
                    }
                },
                "sample_sentences": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "sentence": { "type": "string" },
                            "translation": { "type": "string" },
                            "structure_analysis": { "type": "string" }
                        },
                        "required": ["sentence", "translation"]
                    }
                },
                "generation_parameters": {
                    "type": "object",
                    "properties": {
                        "model_version": { "type": "string" },
                        "temperature": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 2
                        },
                        "top_k": {
                            "type": "integer",
                            "minimum": 1
                        }
                    },
                    "required": ["model_version"]
                }
            },
            "additionalProperties": false
        }
    }
}
```