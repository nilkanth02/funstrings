# StringFun Tests

This directory contains tests for the StringFun package. These tests ensure that all functions in the package work correctly.

## Running Tests

To run the tests, you need to have pytest installed. You can install it with:

```bash
pip install pytest
```

Then, from the project root directory, run:

```bash
pytest
```

Or to run with coverage:

```bash
pytest --cov=stringfun
```

## Test Files

- `test_operations.py`: Tests for the string operation functions

## For Students and Beginners

Testing is an important part of software development. Here's why:

1. **Verify Correctness**: Tests ensure your code works as expected
2. **Prevent Regressions**: Tests catch bugs when you make changes
3. **Document Behavior**: Tests show how functions should be used
4. **Enable Refactoring**: Tests give confidence when improving code

When writing tests:
- Test both normal cases and edge cases
- Make each test focus on one specific thing
- Use descriptive test names that explain what's being tested
- Keep tests independent of each other

## Writing Your Own Tests

To write a new test:

1. Create a new file named `test_*.py`
2. Import the functions you want to test
3. Write test functions that start with `test_`
4. Use assertions to check if functions behave correctly

Example:

```python
def test_reverse_string():
    from stringfun import reverse_string
    
    # Test normal case
    assert reverse_string("hello") == "olleh"
    
    # Test empty string
    assert reverse_string("") == ""
    
    # Test with spaces
    assert reverse_string("hello world") == "dlrow olleh"
```
