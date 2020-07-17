import os
from typing import List


def read_symbols(path: str, sort=False) -> List[str]:
    assert os.path.exists(path)

    symbols = []
    for line in open(path):
        if line.startswith(' '):
            symbols.append(' ')
            continue
        if line.startswith('#'):
            continue
        line = line.strip()
        if not line:
            continue
        symbols.append(line)
    if sort:
        symbols.sort()
    return symbols
