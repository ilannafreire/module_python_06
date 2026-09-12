# 🧪 Python Module 06 — The Codex: Import Mysteries

This project is part of the **42 School Common Core** and focuses on Python
modules, packages, and the import system.

Using a themed alchemy laboratory, the project demonstrates how to organize
code into reusable modules, expose a controlled package interface, navigate
nested packages, and identify circular dependencies.

The main goal is to understand how Python imports work, not to implement
complex algorithms.

This module covers:

- Python packages and `__init__.py`
- module organization and public interfaces
- `import` and `from ... import ...`
- aliases with `as`
- absolute and relative imports
- circular dependencies and late imports
- type annotations and code quality with `flake8` and `mypy`

---

## Project Structure

The project is organized at the repository root and contains the `alchemy`
package:

```text
.
├── elements.py
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── transmutation/
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── grimoire/
│       ├── __init__.py
│       ├── light_spellbook.py
│       ├── light_validator.py
│       ├── dark_spellbook.py
│       └── dark_validator.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_alembic_2.py
├── ft_alembic_3.py
├── ft_alembic_4.py
├── ft_alembic_5.py
├── ft_distillation_0.py
├── ft_distillation_1.py
├── ft_transmutation_0.py
├── ft_transmutation_1.py
├── ft_transmutation_2.py
├── ft_kaboom_0.py
└── ft_kaboom_1.py
```

The `ft_*.py` files are demonstration scripts used to test each import path
and each part of the laboratory.

---

## Exercises Overview

### **Part I — The Alembic**

Introduces modules, packages, and the `__init__.py` interface.

- Creates fire and water in the root `elements.py` module
- Creates earth and air in `alchemy/elements.py`
- Demonstrates `import` and `from ... import ...`
- Shows how `alchemy/__init__.py` controls exposed functions

**Scripts:** `ft_alembic_0.py` through `ft_alembic_5.py`

**Concepts:** modules, packages, package initialization, interface control,
attribute access

`ft_alembic_4.py` intentionally raises an `AttributeError` when it tries to
access `create_earth()` through `alchemy`, because that function is not part of
the package interface.

---

### **Part II — Distillation**

Builds reusable potion functions from the elemental modules.

- `healing_potion()` combines earth and air
- `strength_potion()` combines fire and water
- Exposes the `heal` alias through `alchemy/__init__.py`
- Demonstrates direct module access and package-level access

**Scripts:** `ft_distillation_0.py` and `ft_distillation_1.py`

**Concepts:** code reuse, imports, aliases, package interfaces, function
composition

---

### **Part III — The Great Transmutation**

Explores absolute and relative imports inside a nested package.

- Creates the `alchemy.transmutation` subpackage
- Implements `lead_to_gold()` in `recipes.py`
- Uses absolute imports such as `from alchemy.elements import ...`
- Uses relative imports such as `from ..potions import ...`
- Reaches the same recipe through three different import paths

**Scripts:** `ft_transmutation_0.py`, `ft_transmutation_1.py`, and
`ft_transmutation_2.py`

**Concepts:** nested packages, absolute imports, relative imports, package
navigation, re-exporting

---

### **Part IV — Avoid the Explosion**

Demonstrates how circular dependencies occur and how they can be avoided.

The light magic implementation uses a late import inside the validator
function. This allows the spellbook and validator to work without a circular
import during module initialization.

The dark magic implementation intentionally imports both modules at the top
level. Importing it raises an `ImportError` caused by a circular dependency,
as required by the subject.

**Scripts:** `ft_kaboom_0.py` and `ft_kaboom_1.py`

**Concepts:** dependency design, circular imports, partially initialized
modules, late imports, validation

---

## How to Run

Use Python 3.10 or later from the repository root:

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py
python3 ft_alembic_2.py
python3 ft_alembic_3.py
python3 ft_alembic_4.py
python3 ft_alembic_5.py
```

Run the remaining demonstrations:

```bash
python3 ft_distillation_0.py
python3 ft_distillation_1.py
python3 ft_transmutation_0.py
python3 ft_transmutation_1.py
python3 ft_transmutation_2.py
python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

The following two scripts are expected to fail for educational purposes:

- `ft_alembic_4.py` raises `AttributeError` for the hidden `create_earth()`.
- `ft_kaboom_1.py` raises `ImportError` because of the dark magic circular
	dependency.

---

## Code Quality

Run the static checks with:

```bash
flake8 .
mypy .
```

The project follows these rules:

- Python 3.10 or later
- type annotations on functions
- `flake8`-compatible formatting
- type checking with `mypy`, with the intentional error in `ft_alembic_4.py`
- no `eval()` or `exec()`
- no modification of `sys.path`
- imports only from modules created for this project

`flake8 .` should finish without messages. Running `mypy .` reports one
intentional error because `ft_alembic_4.py` accesses `alchemy.create_earth()`,
which is deliberately not exposed by `alchemy/__init__.py`.

---

## Key Learning Points

- `__init__.py` defines and organizes a package interface.
- Import syntax affects how code is accessed and structured.
- Absolute imports make the complete module path explicit.
- Relative imports help navigate code inside a package.
- Aliases provide convenient public names without duplicating functions.
- Circular dependencies happen during module initialization.
- A late import can break a circular dependency when used carefully.
- Simple functions are enough to demonstrate important architectural concepts.

---

## Expected Results

The successful scripts print messages for created elements, brewed potions,
transmutation recipes, and recorded light spells.

The two intentional error cases demonstrate:

```text
AttributeError: module 'alchemy' has no attribute 'create_earth'
```

and:

```text
ImportError: cannot import name ... from partially initialized module
```

These errors are part of the exercise and should not be removed.