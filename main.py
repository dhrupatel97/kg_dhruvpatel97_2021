from typing import Dict, List


def character_mapping(s1: str, s2: str) -> bool:
    maps = {}

    l1: int = len(s1)
    l2: int = len(s2)

    lst1: List[str] = list(s1)
    lst2: List[str] = list(s2)

    if l1 != l2:
        return False
    else:
        # mapping each character of string 1 to string 2
        [maps.setdefault(i,j) for i,j in zip(lst1, lst2)]
        
        # changing string 1 to get string 2 to check for mapping characters
        s3 = ''.join(maps[c] if c in maps else c for c in s1)

    if s3 == s2:
        return True
    else:
        return False


