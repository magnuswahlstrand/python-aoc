from typing import List

def read_input(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return file.read().splitlines()
