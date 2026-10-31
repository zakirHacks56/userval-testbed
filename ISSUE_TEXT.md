## Issue title

`validate_username` accepts empty and whitespace-only usernames

## Issue body (paste this into the GitHub issue)

**Bug**

`validate_username` in `src/userval/validators.py` is documented to reject empty
or whitespace-only usernames, but it currently returns an empty string instead of
raising `ValueError`.

**Steps to reproduce**

```python
from userval import validate_username

validate_username("")      # returns ""  (expected: ValueError)
validate_username("   ")   # returns ""  (expected: ValueError)
```

**Expected behaviour**

Both calls raise `ValueError("username must not be empty")`.

**Actual behaviour**

Both calls return `""` without raising.

**Acceptance criteria**

- `validate_username("")` raises `ValueError`
- `validate_username("   ")` raises `ValueError`
- existing behaviour for valid names, `None`, non-strings and too-long names is unchanged
- tests in `tests/test_validators.py` pass (`pytest`)

**Hint**

The check should happen after stripping whitespace and before the length check.
