# csum

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/csum?color=brightgreen)](https://pypi.org/project/csum)

## Introduction

`csum` is a CLI program which allows you to to verify checksums. The goal of `csum` is to minimise the effort required when you download a file and want to verify the checksum.

The advantages of `csum` over the native checksum utilites are as follows:

- You don't have to compare checkums by eye, which might be required on some platforms.
- It's easier to type.
- It's the same on all platforms.
- You don't have to type which checksum algorithm is being used.

`csum` supports the most common checksum algorithms:

- `MD5`
- `SHA256`
- `SHA512`
- `SHA1`

In addition, it supports `SHA3_512`, `SHA224`, `BLAKE2S`, `SHA3_224`, `SHA3_256`, `SHA3_384`, `SHA384` and `BLAKE2B`.

## Requirements

You need to have Python 3.6 or higher installed. This will allow you to install `csum` with Python's package manager, `pip`. 

## How to install 

To install `csum` with `pip`, run the command:

```bash
pip install csum
```

After this command completes, the `csum` executable should be available on the PATH.

# Quick start

`csum` is designed to be as simple to use as possible. For this reason, you don't need to specify the checksum type (e.g. `sha256`); `csum` will iterate through the most common types first.

When you use `csum`, the response will be something like:

```bash
        --------------------------------------------------------------------------------

        File: file.zip
        Algorithm: SHA256

        Expected checksum:    40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2
        Calculated checksum:  40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2

        Checksums match ✔

        --------------------------------------------------------------------------------

SUCCESS: SHA256 checksum matched file.
```

## Usage examples

### File and checksum

You can call `csum` with a filename and expected checksum:

```bash
csum file.zip 40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2
```

Or an expected checksum and filename:

```bash
csum 40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2  file.zip 
```

Absolute or relative paths, and paths including tilde (`~`), are accepted:

```bash
csum ~/Downloads/file.zip 40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2  
```

### Preformatted checksum/filename

Sometimes you are provided with an expected checksum of the form:

`40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2  file.zip`

Assuming that the file is in the current working directory, you can simply copy this text and paste it after the `csum` command:

```bash
csum 40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2  file.zip
```

If you prefer, you can supply it as a single argument:

```bash
csum "40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2  file.zip"
```

> **Tip**: The number of spaces between the checksum and filename doesn't matter in either case.

### Manually choosing an algorithm

If you prefer to select a particular algorithm instead of iterating through them, you can use the `-a`/`--algorithm` parameter.

For example, using the SHA256 algorithm only:

```bash
csum -a sha256 file.zip 40f66f20b1ecb05cb11a9627520aafafbc8cd86b33eb8019cbea9925d8ca83ce2
```

> **Tip:** You can provide the algorithm name as either lower-case or upper-case, e.g. `sha256` or `SHA256`.

# License

You may freely use, modify and redistribute this program under the terms of the MIT License. See [LICENSE](https://github.com/CabbageDevelopment/csum/blob/master/LICENSE).