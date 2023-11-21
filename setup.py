from setuptools import setup

setup(
    name="proofivy-cli-app",
    version="0.2.0",
    description="Proofivy app to calculate hashes of files",
    py_modules=["proofivy"],
    entry_points={
        "console_scripts": [
            "proofivy = proofivy:main",
        ]
    },
)
