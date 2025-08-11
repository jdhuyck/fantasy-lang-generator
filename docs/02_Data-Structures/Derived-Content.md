## Purpose
Stores ML-generated content that's derived from other language components.

## Schema

```typescript
interface DerivedContent {
    generated_words: Array<{
        word: string;
        meaning: string;
        components: string[];
        confidence: number;  // 0-1
    }>;
    sample_sentences: Array<{
        sentence: string;
        translation: string;
        structure_analysis: string;
    }>;
    generation_parameters: {
        model_version: string;
        temperature?: number;
        top_k?: number;
    };
}
```