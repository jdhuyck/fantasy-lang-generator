## Purpose
Types used for responses to API

## Schema
```typescript
interface ForkResponse {
    new_language_id: string;
    source_version: number;
    forked_at: string;
    changes_applied: string[];  // Paths of modified fields
}

interface VersionDiff {
    base_version: number;
    target_version: number;
    changes: ChangeRecord[];
}

interface ChangeRecord {
    path: string;  // JSON path e.g. "phonology.consonants.stops
    op: "add" | "remove" | "replace";
    value?: any;
    old_value?: any;
    timestamp: string;
}

// GET /languages
interface LanguageListResponse {
    languages: Array<{
        id: string;
        name: string;
        creator: string;
        created_at: string;
        version: number;
        description?: string;
        tags: string[];
        is_template?: boolean;
    }>;
    pagination?: {
        total: number;
        limit: number;
        offset: number;
    }
}

// GET /templates
interface TemplateResponse {
    templates: Array<{
        id: string;
        name: string;
        description: string;
        creator: string;
        tags: string[];
        preview?: {
            sample_word: string;
            sample_sentence: string;
        };
    }>;
}

// GET /languages/{id}/diff/{version}
interface LanguageDiffResponse {
    base_version: number;
    target_version: number;
    changes: Array<{
        path: string;  // JSON Path e.g. "phonology.consonants.stops"
        operation: "added" | "removed" | "modified";
        old_value?: any;
        new_value?: any;
        changed_by: string;
        changed_at: string;
    }>;
    affected_components: Array<"phonology" | "vocabulary" | "grammar" | "culture">;
}

// POST /languages/{id}/fork
interface LanguageForkResponse {
    new_language_id: string;
    source_language: {
        id: string;
        version: number;
        name: string;
    };
    forked_at: string;
    inherited_components: Array<{
        component: string;
        version: string;
    }>;
    modified_components?: Array<{
        component: string;
        changes: number;
    }>;
}

// POST /generate/words
interface WordGenerationResponse {
    words: Array<{
        word: string;
        meaning: string;
        component: string[];
        phonetic_transcription?: string;
        confidence: number;
        source_rules?: {
            phonology?: string[];
            morphology?: string[];
        };
    }>;
    warnings?: Array<{
        code: string;
        message: string;
        context?: any;
    }>;
}

// POST /generate/sentences
interface SentenceGenerationResponse {
    sentences: Array<{
        sentence: string;
        translation: string;
        structure: {
            diagram?: string;
            analysis: string;
        }
        words: Array<{
            original: string;
            root_form: string;
            grammatical_tags: string[];
        }>;
    }>;
    complexity_metrics?: {
        avg_word_length: number;
        unique_words: number;
        sentence_structure;
    };
}

// POST /validate
interface ValidationResponse {
    valid: boolean;
    errors?: Array<{
        path: string;
        code: string;
        message: string;
        severity: "error" | "warning" | "info";
        suggested_fix?: string;
    }>;
    schema_version: string;
    validated_components: Array<{
        component: string;
        valid: boolean;
        error_count?: number;
    }>;
}

// PATCH /languages/{id}/phonology
interface PhonologyUpdateResponse {
    updated: {
        consonants: boolean;
        vowels: boolean;
        syllable: boolean;
        phonotactics: boolean;
    };
    generated_artifacts?: {
        sample_words?: string[];
        syllable_examples: string[];
    };
    version: number;
}

// PATCH /languages/{id}/vocabulary
interface VocabularyUpdateResponse {
    added: number;
    modified: number;
    removed: number;
    semantic_fields_updated: string[];
    generation_triggers?: {
        derived_words?: number;
        example_sentences?: number;
    };
    version: number;
}

// GET /languages/{id}/export
interface LanguageExportResponse {
    file_type: "json" | "yaml" | "csv";
    download_url: string;
    expires_at?: string;
    includes: Array<"metadata" | "phonology" | "vocabulary" | "grammar" | "culture" | "generated">;
    version: number;
}


// Utility types
interface Pagination {
    total: number;
    limit: number;
    offset: number;
}

interface ErrorResponse {
    error: {
        code: string;
        message: string;
        details?: any;
    };
    request_id?: string;
}

interface VersionInfo {
    current: number;
    latest: number;
    last_modified: string;
    modified_by: string;
}
```