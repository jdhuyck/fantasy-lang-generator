## Language Resources - `/api/v1`

### `GET /languages`
- List all created languages
- Response: `200 OK` with `{ languages: LanguageMeta[] }`

### `POST /languages`
- Create a new language
- Body: `{ language_name: string, creator: string }`
- Response: `201 Created` with full language object

### `GET /languages/{language_id}`
- Get complete language definition
- Response: `200 OK` with full language JSON

### `POST /languages/{language_id}`
- Update entire language definition
- Body: Complete language JSON
- Response: `200 OK` with update language

### `DELETE /languages/{language_id}`
- Delete a language
- Response: `204 No Content`


## Component-Specific Endpoints

### `PATCH /languages/{language_id}/phonology`
- Update just phonology
- Body: Phonology JSON
- Response: `200 OK` with updated component

### `PATCH /languages/{language_id}/vocabulary`
- Update vocabulary
- Body: Vocabulary JSON
- Response: `200 OK` with updated component

### `GET /languages/{language_id}/export`
- Export language as downloadable JSON
- Response: `200 OK` with `Content-Disposition: attachment`


## Generation Endpoints

### `POST /generate/words`
- Generate new words
- Body: `{
    language_id: string,
    count: number,
    constraints?: {
        min_syllables?: number,
        semantic_field?: string
    }
}`
- Response: `200 OK` with `{ words: GeneratedWord[]  }`

### `POST /generate/sentences`
- Generate example sentences
- Body `{
    language_id: string,
    count: number,
    complexity?: "simple" | "complex"
}`
- Response: `200 OK` with `{ sentences: GeneratedSentence[] }


## Validation Endpoint

### `POST /validate`
- Validate language structure
- Body: Complete language JSON
- Response: `200 OK` with `{
    valid: boolean,
    errors?: ValidationError[]
}`