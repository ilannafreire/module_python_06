def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    normalized = ingredients.lower()
    valid = any(
        ingredient in normalized
        for ingredient in light_spell_allowed_ingredients()
    )
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
