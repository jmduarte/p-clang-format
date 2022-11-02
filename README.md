clang-format mirror
===================

Mirror of `clang-format` package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For p-clang-format: see https://github.com/MedicineYeh/p-clang-format


### Using clang-format with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
-   repo: https://github.com/jmduarte/p-clang-format
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: p-clang-format
```
