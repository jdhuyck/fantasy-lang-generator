# Complete Dwarven Language Example

```json
{
    "metadata": {
        "language_name": "Khazadûl",
        "creator": "tolkien",
        "created_at": "1954-07-29T00:00:00Z",
        "version": 1.0,
        "tags": ["dwarves", "middle-earth"]
    },
    "phonology" : {
        "consonants": {
            "stops": ["b", "d", "g", "kh"],
            "fricatives": ["f", "th", "zh"],
            "nasals": ["m", "n"],
            "liquids": ["r", "l"],
            "constraints": {
                "initial_clusters": ["dr", "gr", "kh"],
                "forbidden_clusters": ["fn", "thm"]
            }
        },
        "vowels": {
            "short": ["a", "e", "i", "o", "u"],
            "long": ["â", "ê", "î", "ô", "û"]
        }
    }
}
```