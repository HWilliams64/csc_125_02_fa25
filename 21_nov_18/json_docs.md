JSON => JavaScript Object Notation
 - This a light weight data-interchange format that is easy for humans to read
   and write, and easy for machines to parse and generate.

Example JSON Object:
```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Science", "History"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "zip": "12345"
  }
}
```

Example JSON Array:
```json
[
  {
    "name": "Alice",
    "age": 25
  },
  {
    "name": "Bob",
    "age": 28
  }
]
```

Difference between python Dict and JSON:
- Python Dicts can have non-string keys, while JSON keys must be strings.
- Python single and double quotes are interchangeable, while JSON requires
  double quotes for strings.
- Python supports comments, while JSON does not allow comments. (Except jsonc => JSON with Comments)
- Python uses `True`, and `False`, while JSON uses `true`, and `false`. The
  difference is in the casing
- Python uses `None` while JSON uses `null`. They mean the same thing.
