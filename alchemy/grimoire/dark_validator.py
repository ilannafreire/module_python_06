from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized = ingredients.lower()
    valid = any(
        ingredient in normalized
        for ingredient in dark_spell_allowed_ingredients()
    )
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
