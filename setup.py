from setuptools import setup, Extension, find_packages

extModules = [
    Extension(
        "tgcrypto",
        sources=[
            "tgcrypto/tgcrypto.c",
            "tgcrypto/aes256.c",
            "tgcrypto/ige256.c",
            "tgcrypto/ctr256.c",
            "tgcrypto/cbc256.c"
        ],
    )
]

setup(
    packages=find_packages(),
    ext_modules=extModules
)
