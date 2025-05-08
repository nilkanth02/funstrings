# Contributing to FunStrings

First off, thank you for considering contributing to FunStrings! It's people like you that make FunStrings such a great tool for students, educators, and developers.

This document provides guidelines and instructions for contributing to this project. By participating in this project, you agree to abide by its terms.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Development Environment](#development-environment)
  - [Project Structure](#project-structure)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Adding New Functions](#adding-new-functions)
  - [Improving Documentation](#improving-documentation)
  - [Writing Tutorials](#writing-tutorials)
  - [Creating Examples](#creating-examples)
- [Development Workflow](#development-workflow)
  - [Fork and Clone](#fork-and-clone)
  - [Create a Branch](#create-a-branch)
  - [Make Your Changes](#make-your-changes)
  - [Test Your Changes](#test-your-changes)
  - [Submit a Pull Request](#submit-a-pull-request)
- [Coding Standards](#coding-standards)
  - [Style Guide](#style-guide)
  - [Documentation](#documentation)
  - [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

## Code of Conduct

This project and everyone participating in it is governed by the FunStrings Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [Author](mailto:nilkanth8747@gmail.com).

## Project Overview

FunStrings is a Python package that provides a wide range of functions for string manipulation, analysis, and transformation with a focus on AI and data science applications. The library serves as a foundational tool for text preprocessing in natural language processing (NLP), machine learning pipelines, and data analysis workflows.

Key aspects of the project:

- **NLP Preprocessing**: Functions for text normalization, tokenization, and feature extraction that prepare text data for machine learning models
- **Data Cleaning**: Tools to sanitize and standardize text data from various sources
- **Feature Engineering**: Utilities to extract meaningful features from text for ML models
- **Educational Focus**: Designed to be accessible for students and practitioners learning data science and AI
- **Production Ready**: Optimized for use in real-world data science pipelines

FunStrings bridges the gap between raw text data and AI-ready datasets, making it an essential tool for data scientists, ML engineers, and AI researchers while remaining approachable for beginners in the field.

## Getting Started

### Development Environment

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/funstrings.git
   cd funstrings
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install development dependencies**:
   ```bash
   pip install -e ".[dev]"
   ```

### Project Structure

- `funstrings/`: Main package directory
  - `__init__.py`: Package initialization and exports
  - `operations.py`: Core string operation functions
  - `__main__.py`: Command-line interface
- `tests/`: Test directory
  - `test_operations.py`: Tests for basic operations
  - `test_new_operations.py`: Tests for advanced operations
  - `test_new_functions.py`: Tests for newer functions
- `docs/`: Documentation
- `examples/`: Example scripts
- `tutorials/`: Educational tutorials

## How to Contribute

There are many ways to contribute to FunStrings, even if you're not a Python expert!

### Reporting Bugs

If you find a bug, please create an issue on GitHub with:

1. A clear, descriptive title
2. A detailed description of the issue
3. Steps to reproduce the bug
4. Expected behavior
5. Actual behavior
6. Your environment (Python version, OS, etc.)

### Suggesting Enhancements

Have an idea for a new feature or improvement? Create an issue with:

1. A clear, descriptive title
2. A detailed description of your suggestion
3. Examples of how the feature would work
4. Why this enhancement would be useful

### Adding New Functions

FunStrings is always looking for new string manipulation functions! To add a new function:

1. Check if a similar function already exists
2. Create a new function in `operations.py`
3. Add comprehensive docstrings with examples
4. Write tests for your function in the appropriate test file
5. Update `__init__.py` to export your function
6. Add your function to the README.md

### Improving Documentation

Good documentation is crucial for an educational package:

1. Improve existing docstrings
2. Add more examples to function documentation
3. Create or improve markdown files in the `docs/` directory
4. Fix typos or clarify explanations

### Writing Tutorials

Tutorials help users learn how to use FunStrings effectively:

1. Create new tutorial scripts in the `tutorials/` directory
2. Focus on specific use cases or learning objectives
3. Include detailed comments explaining each step
4. Make sure tutorials are beginner-friendly

### Creating Examples

Examples show how to use FunStrings in real-world scenarios:

1. Add example scripts to the `examples/` directory
2. Focus on practical applications
3. Include comments explaining the code
4. Ensure examples are easy to understand

## Development Workflow

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/funstrings.git
   cd funstrings
   ```
3. Add the original repository as an upstream remote:
   ```bash
   git remote add upstream https://github.com/nilkanth02/funstrings.git
   ```

### Create a Branch

Create a branch for your work:
```bash
git checkout -b feature/your-feature-name
```

Use a descriptive branch name that reflects your changes.

### Make Your Changes

1. Make your changes to the codebase
2. Follow the [coding standards](#coding-standards)
3. Add or update tests as needed
4. Add or update documentation as needed

### Test Your Changes

Run the tests to make sure everything works:
```bash
pytest
```

For test coverage:
```bash
pytest --cov=funstrings
```

### Submit a Pull Request

1. Push your changes to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Go to the original repository on GitHub
3. Create a new pull request from your branch
4. Provide a clear description of your changes
5. Reference any related issues

## Coding Standards

### Style Guide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use 4 spaces for indentation (no tabs)
- Keep line length to a maximum of 88 characters
- Use meaningful variable and function names
- Add comments for complex code sections

### Documentation

- All functions should have docstrings following the [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Include examples in docstrings
- Use type hints for function parameters and return values
- Keep documentation up-to-date with code changes

### Testing

- Write tests for all new functions
- Ensure tests cover both normal cases and edge cases
- Maintain or improve test coverage
- Make sure all tests pass before submitting a pull request

## Pull Request Process

1. Ensure your code follows the project's coding standards
2. Update documentation as needed
3. Add or update tests as needed
4. Make sure all tests pass
5. Submit your pull request with a clear description
6. Respond to any feedback or requested changes

## Community

- Join discussions in GitHub issues
- Help answer questions from other contributors
- Share your experience using FunStrings
- Spread the word about the project

Thank you for contributing to FunStrings! Your efforts help make this project better for everyone.
