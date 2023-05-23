# Proofivy cli app

Calculate BLAKE3 hash of a file and return [CID](https://docs.ipfs.tech/concepts/content-addressing/):
```commandline
python proofivy.py filename
❯ bafkr4if3dele6mey6vfrfmctwzmoxwonziolrwa7tohflbiln4znto2lvu
```

## pip install
In the repo folder:
```commandline
pip install .
```
Then use:
```commandline
proofivy filename
❯ bafkr4if3dele6mey6vfrfmctwzmoxwonziolrwa7tohflbiln4znto2lvu
```

## Notes
- Uses [BLAKE3 Python library](https://github.com/oconnor663/blake3-py)
- Includes code snippets from [this repo](https://github.com/thunderstore-io/ipfs-cid) for CID creation
