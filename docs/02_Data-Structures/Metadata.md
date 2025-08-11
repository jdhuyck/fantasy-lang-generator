## Purpose
Contains administrative information about the language.

## Schema

```typescript
interface Metadata {
    language_name: string;
    creator: string;
    created_at: ISO8601String;
    last_modified: ISO8601String;
    version: number;
    description?: string;
    tags: string[];

    parent_id?: string;
    original_creator?: string;
    version_history: VersionHistoryEntry[];
}
```