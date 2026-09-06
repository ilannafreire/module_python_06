from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    status = "VALID" if validation.endswith("VALID") else "INVALID"
    action = "recorded" if status == "VALID" else "rejected"
    return f"Spell {action}: {spell_name} ({validation})"
