import itertools
from typing import List, Tuple

# Given a list of system attributes, generate all possible unordered conflict pairs
def enumerate_conflict_pairs(attributes: List[str]) -> List[Tuple[str, str]]:
    return list(itertools.combinations(attributes, 2))

# Optional: filter conflicts based on keyword heuristics or known rules (stub for now)
def filter_conflicts(pairs: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    # For now, we don't filter—assume all pairs could potentially have a conflict
    return pairs

# Example usage
if __name__ == "__main__":
    sample_attributes = [
        "cooking speed",
        "temperature consistency",
        "robot arm precision",
        "food packaging integrity",
        "order processing time",
        "system energy usage"
    ]

    raw_pairs = enumerate_conflict_pairs(sample_attributes)
    final_pairs = filter_conflicts(raw_pairs)

    print("Generated Conflict Pairs:")
    for i, (a, b) in enumerate(final_pairs):
        print(f"{i+1}. {a} vs {b}")
