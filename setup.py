from pathlib import Path

from setuptools import find_packages, setup

README = Path(__file__).parent / "README.md"

setup(
    name="starpatterns",
    version="0.1.0",
    description="ASCII patterns, fractals, and terminal animations with no dependencies.",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="Starpatterns contributors",
    license="MIT",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Intended Audience :: Developers",
        "Topic :: Artistic Software",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
    ],
    project_urls={
        "Documentation": "https://pypi.org/project/starpatterns/",
        "Source": "https://pypi.org/project/starpatterns/",
    },
)
