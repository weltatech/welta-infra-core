# schemas/asset_struct.py

# Placeholder schema for tokenizable infrastructure assets.
# Simulates the structure used in AI alignment and token logic layers.

ASSET_SCHEMA = {
    "type": "object",
    "properties": {
        "asset_id": {"type": "string"},
        "region": {"type": "string"},
        "zoning_level": {"type": "string"},
        "asset_class": {"type": "string"},
        "compliance_score": {"type": "number"},
        "metadata": {"type": "object"}
    },
    "required": ["asset_id", "region", "zoning_level"]
}
