from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aim-memory",
    version="1.0.0",
    author="Brian Vasquez",
    description="A standalone RAG 5.21 memory engine featuring LanceDB, Tantivy FTS, and an Entity Intersection Reranker.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BrianV1981/aim-memory",
    packages=find_packages(exclude=["benchmarks", "benchmarks.*"]),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
