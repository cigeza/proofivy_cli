# Includes code from:
# https://github.com/thunderstore-io/ipfs-cid

from blake3 import blake3
from base64 import b32encode
import argparse

MULTICODEC_CIDV1 = b"\x01"
MULTICODEC_RAW_BINARY = b"\x55"
MULTICODEC_LENGTH_256 = b"\x20"
MULTICODEC_BLAKE3 = b"\x1e"
PREFIX = "b"

CID_PREFIX = b"".join(
    [
        MULTICODEC_CIDV1,
        MULTICODEC_RAW_BINARY,
        MULTICODEC_BLAKE3,
        MULTICODEC_LENGTH_256,
    ],
)


def encode(data: bytes) -> str:
    b32 = b32encode(data).decode()
    return PREFIX + b32.lower().replace("=", "")


def cid_sha256_wrap_digest(digest: bytes) -> str:
    digest_len = len(digest).to_bytes(1, "big")
    if digest_len != MULTICODEC_LENGTH_256:
        raise AttributeError("Invalid digest length")
    return encode(CID_PREFIX + digest)


def main():
    parser = argparse.ArgumentParser(epilog="PROOFIVY - https://proofivy.com")
    parser.add_argument("filename", help="file directory for BLAKE3 hash calculation")
    args = parser.parse_args()
    with open(args.filename, mode='rb') as file:
        file_to_hash = file.read()
    blake3_file = blake3(file_to_hash).digest()
    hash_string = cid_sha256_wrap_digest(blake3_file)
    print(f"{hash_string}")


if __name__ == "__main__":
    main()
