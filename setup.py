from setuptools import setup

setup(
    name="proofivy-cli-app",
    version="0.1.0",
    description="Proofivy app to calculate BLAKE3 hashes of files",
    py_modules=["proofivy"],
    entry_points={
        "console_scripts": [
            "proofivy = proofivy:main",
        ]
    },
)
