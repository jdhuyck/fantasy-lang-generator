## Purpose
Documents how a culture shapes language development, affecting:
- Word connotations
- Taboo terms
- Specialized vocabulary
- Grammatical emphasis

## Schema

```typescript
interface CulturalInfluences {
    environment: EnvironmentType;
    technology_level: number;  // 1-10 scale
    social_structure: SocialStructureType;
    values: string[];
    taboos: string[];
    contact_languages: string[];
}

type EnvironmentType =
    | "mountainous"
    | "forest"
    | "desert"
    | "coastal"
    | "urban"
    | "underground";

type SocialStructureType = 
    | "clan_hierarchy"
    | "egalitarian"
    | "matriarchal"
    | "imperial"
    | "tribal";
```