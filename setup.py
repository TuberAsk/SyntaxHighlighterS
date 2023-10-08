from setuptools import setup, find_packages

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="SyntaxHighlighterS",
    version="0.0.3",
    description="A Simple Starter Syntax Highlighter.",
    author="TuberAsk",
    packages=find_packages(where="src"),  # Specify the 'src' directory as the package root
    package_dir={"": "src"},  # Specify the package directory mapping
    long_description=long_description,  # Use the README content as long description
    long_description_content_type="text/markdown",  # Specify the README file type
    project_urls = {
        "Homepage": "https://github.com/TuberAsk/SyntaxHighlighterS",
        "Documentation": "https://github.com/TuberAsk/SyntaxHighlighterS/wiki",
        "Funding": "https://patreon.com/isitopensource",
        "Bug Tracker": "https://github.com/TuberAsk/SyntaxHighlighterS/issues",
    },
)
