## Word Storage Approach

```mermaid
graph LR
    A[Vocabulary] --> B[Base Words]
    A --> C[Word Formation]
    A --> D[Semantic Fields]
```

## Schemas

```typescript
interface Vocabulary {
    base_words: Record<string, string>;
    word_formation_rules: {
        diminutive?: string;
        augmentative?: string;
        material?: string;
    };
    semantic_fields: Record<string, Record<string, string>>;
}
```