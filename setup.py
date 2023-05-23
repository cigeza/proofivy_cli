from setuptools import setup

setup(
    name="proofivy-cli-app",
    version="0.1.0",
    description="Proofivy app to calculate BLAKE3 hashes of files",
    # The Python file that contains your CLI app
    py_modules=["proofivy"],
    # The entry point for your CLI app
    entry_points={
        "console_scripts": [
            "proofivy = proofivy:main",
        ]
    },
)
