"""Setup script for the funstrings package.

This file contains all the package metadata required for distributing and installing
the package using pip. It follows the setuptools conventions for Python packaging.

For beginners and students:
- This file is the standard way to package Python code for distribution
- It defines metadata about your package (name, version, author, etc.)
- It specifies dependencies that your package needs to run
- It configures how your package should be installed

To use this file:
1. Install your package locally: pip install -e .
2. Build distribution files: python setup.py sdist bdist_wheel
3. Upload to PyPI: python -m twine upload dist/*

Learn more about Python packaging at:
https://packaging.python.org/tutorials/packaging-projects/
"""

# Import required functions from setuptools
from setuptools import setup, find_packages

# Read the contents of README.md file to use as the long description
# This will appear on the PyPI project page
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Call the setup function with our package metadata
setup(
    #############################################
    # BASIC PACKAGE INFORMATION
    #############################################

    # Package name - this is how users will refer to your package when installing
    # Example: pip install funstrings
    name="funstrings",

    # Version number - follow semantic versioning (MAJOR.MINOR.PATCH)
    version="0.1.0",

    #############################################
    # PACKAGE DESCRIPTION
    #############################################

    # Short description (appears in PyPI search results)
    description="A Python package for string manipulation and analysis, and to play with strings",

    # Long description (appears on PyPI project page)
    # We're using the content from README.md
    long_description=long_description,

    # Specify the format of the long description
    # Options include: text/markdown, text/x-rst, text/plain
    long_description_content_type="text/markdown",

    #############################################
    # LINKS AND CONTACT INFORMATION
    #############################################

    # Homepage URL for your project
    # This typically points to your GitHub repository or documentation
    url="https://github.com/nilkanth02/funstrings",

    # Direct download URL for a specific version (optional)
    # download_url="https://github.com/nilkanth02/funstrings/archive/v0.1.0.tar.gz",

    # Author information
    author="Nilkanth Ahire",
    author_email="nilkanth8747@gmail.com",

    #############################################
    # LICENSE INFORMATION
    #############################################

    # License under which your package is distributed
    # Common licenses include: MIT, BSD, Apache, GPL
    # Make sure to include a LICENSE file in your package
    license="MIT",

    #############################################
    # CLASSIFIERS
    #############################################
    # Classifiers help users find your project on PyPI
    # Full list: https://pypi.org/classifiers/
    classifiers=[
        # Development status
        # Options: 1-Planning, 2-Pre-Alpha, 3-Alpha, 4-Beta, 5-Production/Stable, 6-Mature, 7-Inactive
        "Development Status :: 3 - Alpha",

        # Intended audience
        "Intended Audience :: Developers",
        "Intended Audience :: Education",  # Added for students
        "Intended Audience :: Science/Research",  # Added for academic use

        # License (should match the license field above)
        "License :: OSI Approved :: MIT License",

        # Natural language support
        "Natural Language :: English",

        # Operating systems
        "Operating System :: OS Independent",  # If your package works on any OS

        # Python versions supported
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

        # Topic
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "Topic :: Education :: Computer Aided Instruction (CAI)",  # Added for educational use
    ],

    #############################################
    # KEYWORDS
    #############################################
    # Keywords help users find your package when searching on PyPI
    keywords="string, text, manipulation, utility, education, learning, beginner, student, playing, fun, easy_working",

    #############################################
    # PACKAGE DISCOVERY AND STRUCTURE
    #############################################
    # find_packages() automatically finds all packages and subpackages
    # by looking for __init__.py files in directories
    packages=find_packages(),

    #############################################
    # PYTHON VERSION REQUIREMENTS
    #############################################
    # Specify which Python versions your package supports
    python_requires=">=3.6",

    #############################################
    # DEPENDENCIES
    #############################################
    # List packages that your package depends on to run
    # These will be installed automatically when your package is installed
    install_requires=[
        # Example: "requests>=2.25.1",
        # Example: "numpy>=1.20.0",
    ],

    #############################################
    # OPTIONAL DEPENDENCIES
    #############################################
    # Define groups of extra dependencies that users can install if needed
    # Example usage: pip install funstrings[dev]
    extras_require={
        # Dependencies for development and testing
        "dev": [
            "pytest>=6.0",      # Testing framework
            "pytest-cov",        # Test coverage reporting
            "flake8",            # Code linting
            "black",             # Code formatting
            "sphinx",            # Documentation generator
            "sphinx-rtd-theme",  # Documentation theme
        ],
        # Dependencies for educational purposes
        "edu": [
            "jupyter",           # For interactive notebooks
            "matplotlib",        # For visualizations
        ],
    },

    #############################################
    # ENTRY POINTS
    #############################################
    # Define command-line scripts that will be installed with your package
    # Format: script_name=package.module:function
    entry_points={
        "console_scripts": [
            # This creates a 'funstrings' command that runs the main() function in __main__.py
            "funstrings=funstrings.__main__:main",
        ],
    },

    #############################################
    # PACKAGE DATA
    #############################################
    # Include non-Python files in your package
    # This requires a MANIFEST.in file to specify which files to include
    include_package_data=True,

    #############################################
    # INSTALLATION OPTIONS
    #############################################
    # If False, package will be installed as a directory rather than a zip file
    # This is usually better for debugging and development
    zip_safe=False,

    #############################################
    # ADDITIONAL PROJECT URLS
    #############################################
    # Additional URLs that will appear on your PyPI project page
    project_urls={
        "Bug Tracker": "https://github.com/nilkanth02/funstrings/issues",
        "Documentation": "https://github.com/nilkanth02/funstrings",
        "Source Code": "https://github.com/nilkanth02/funstrings",
        "Examples": "https://github.com/nilkanth02/funstrings/tree/main/examples",  # Add examples directory
        "Educational Resources": "https://github.com/nilkanth02/funstrings/tree/main/tutorials",  # Add tutorials
    },
)
