## Purpose
Handling versioning and forking.

## Schema
```typescript
interface VersionHistoryEntry{
    version: number;
    modified_at: string;  // ISO8601
    modified_by: string;
    changeset?: string;  // Optional commit message
}

interface LanguageVersion {
    language_id: string;
    version: number;
    snapshot: Language;
    created_at: string;  // ISO8601
    created_by: string;
}

interface LanguageFork {
    fork_id: string;
    source_language_id: string;
    source_version: number;
    new_language_id: string;
    forked_at: string;  // ISO8601
    forked_by: string;
}
```