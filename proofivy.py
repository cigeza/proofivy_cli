# Includes code from:
# https://github.com/thunderstore-io/ipfs-cid

from hashlib import sha256
from blake3 import blake3
from base64 import b32encode
import argparse

MULTICODEC_CIDV1 = b"\x01"
MULTICODEC_RAW_BINARY = b"\x55"
MULTICODEC_SHA_2_256 = b"\x12"
MULTICODEC_BLAKE3 = b"\x1e"
MULTICODEC_LENGTH_256 = b"\x20"
PREFIX = "b"


CID_PREFIX_SHA256 = b"".join(
    [
        MULTICODEC_CIDV1,
        MULTICODEC_RAW_BINARY,
        MULTICODEC_SHA_2_256,
        MULTICODEC_LENGTH_256,
    ],
)

CID_PREFIX_BLAKE3 = b"".join(
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


def cid_wrap_digest_sha256(digest: bytes) -> str:
    digest_len = len(digest).to_bytes(1, "big")
    if digest_len != MULTICODEC_LENGTH_256:
        raise AttributeError("Invalid digest length")
    return encode(CID_PREFIX_SHA256 + digest)


def cid_wrap_digest_blake3(digest: bytes) -> str:
    digest_len = len(digest).to_bytes(1, "big")
    if digest_len != MULTICODEC_LENGTH_256:
        raise AttributeError("Invalid digest length")
    return encode(CID_PREFIX_BLAKE3 + digest)


def main():
    parser = argparse.ArgumentParser(epilog="PROOFIVY - https://proofivy.com")
    parser.add_argument("filename", help="file directory for hash calculation")
    parser.add_argument("--blake3", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    with open(args.filename, mode='rb') as file:
        file_to_hash = file.read()
    if args.blake3:
        blake3_file = blake3(file_to_hash).digest()
        hash_string = cid_wrap_digest_blake3(blake3_file)
        print(f"{hash_string}")
    else:
        sha256_file = sha256(file_to_hash).digest()
        hash_string = cid_wrap_digest_sha256(sha256_file)
        print(f"{hash_string}")


if __name__ == "__main__":
    main()
