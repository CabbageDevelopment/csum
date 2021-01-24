#  MIT License
#
#  Copyright (c) 2021 Cabbage Development
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import hashlib
import os
import re
import sys
from argparse import Namespace
from os.path import abspath, expandvars, expanduser
from typing import Callable

from csum import argparsing

args: Namespace = argparsing.get_args()

algorithms = {}
available = ["md5", "sha256", "sha1", "sha512"]

for a in hashlib.algorithms_guaranteed:
    if a not in available:
        available.append(a)

for a in available:
    func = getattr(hashlib, a)

    if func:
        algorithms[a] = func


def calc_hash(data: bytes, algorithm: Callable) -> str:
    try:
        return algorithm(data).hexdigest()
    except:
        return None


if len(args.args) == 2:
    filename = args.args[0]
    expected = args.args[1]

    if os.path.exists(expected) and not os.path.exists(filename):
        filename, expected = expected, filename

# 38f66f16b0ecb03cb9a9627517aafafbc5cd84b31eb8019cbea9925d8ca83ce2  lineage-17.1-20210123-nightly-beryllium-signed.zip
elif len(args.args) == 1:
    matches = re.findall(r"^\s*([^\s]+)\s+([^\s]+)\s*$", args.args[0])

    if not matches or len(matches[0]) != 2:
        print(f"Cannot parse correct filename and checksum from: {args.args}")
        sys.exit(1)

    expected, filename = matches[0]
else:
    print(f"Invalid input: {args.args}")
    sys.exit(1)

if not os.path.exists(filename):
    print(f"File does not exist: {filename}")
    sys.exit(1)

with open(filename, "rb") as f:
    data = f.read()

expected = expected.lower()
filename = abspath(expandvars(expanduser(filename)))

if args.algorithm:
    func = algorithms.get(args.algorithm)

    if not func:
        print(f"Algorithm not available: {func}")
        sys.exit(1)

    algorithms = {args.algorithm: func}

for name, func in algorithms.items():
    checksum = calc_hash(data, func)

    if expected == checksum:
        print(
            f"""
        --------------------------------------------------------------------------------
        
        File: {filename}
        Algorithm: {name.upper()}
        
        Expected checksum:    {expected}
        Calculated checksum:  {checksum}
        
        Checksums match ✔
        
        --------------------------------------------------------------------------------
        """
        )
        print(f"SUCCESS: {name.upper()} checksum matched file.", end="\n\n")
        sys.exit(0)

    print(f"No match for {name.upper()}... ", end="")
    if not checksum:
        print(f"(Failed to calculate checksum.)")
    else:
        print()
else:
    print(
        f"""
        --------------------------------------------------------------------------------
        
        File: {filename}
        Expected checksum:    {expected}
        
        Checksums do NOT match.
        
        --------------------------------------------------------------------------------
        """
    )
    print(f"FAILED: algorithm(s) did not match the checksum.", end="\n\n")
