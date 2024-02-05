USER_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "per_page": {"type": "number"},
        "total": {"type": "number"},
        "total_pages": {"type": "number"},
        "data": {"type": "array"},
        "support": {"type": "object"}
    },
    "required": ["page"]
}


