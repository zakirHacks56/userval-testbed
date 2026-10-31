# userval

Tiny username validation package.

```python
from userval import validate_username

validate_username("  alice ")   # -> "alice"
validate_username("")           # -> ValueError
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Contributing

Keep changes small and add a regression test for every bug fix.
Only touch files under `src/userval/` and `tests/`.
