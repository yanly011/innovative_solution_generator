import random
from typing import List, Tuple, Dict
import json

# Load TRIZ contradiction matrix from a simple keyword-based mock JSON
# Format: {"attribute_keywords": [("principle_id", "principle_name")...]}
def load_triz_matrix(json_path: str) -> Dict[str, List[Tuple[int, str]]]:
    with open(json_path, 'r') as f:
        return json.load(f)

# Simplistic keyword-matching binder (matches if either attr contains keyword)
def bind_triz_principles(attr_a: str, attr_b: str, triz_matrix: Dict[str, List[Tuple[int, str]]]) -> List[Tuple[int, str]]:
    matched = set()
    for key, principles in triz_matrix.items():
        if key.lower() in attr_a.lower() or key.lower() in attr_b.lower():
            matched.update(principles)
    return list(matched)

# Bind a list of conflict pairs to TRIZ principles
def bind_all_conflicts(pairs: List[Tuple[str, str]], triz_matrix: Dict[str, List[Tuple[int, str]]]) -> List[Dict]:
    results = []
    for a, b in pairs:
        principles = bind_triz_principles(a, b, triz_matrix)
        if not principles:
            # fallback: pick a few random ones for exploration
            all_principles = sum(triz_matrix.values(), [])
            principles = random.sample(all_principles, min(3, len(all_principles)))
        results.append({
            "attribute_a": a,
            "attribute_b": b,
            "principles": principles
        })
    return results

# Example usage
def demo():
    mock_pairs = [
        ("cooking speed", "temperature consistency"),
        ("robot arm precision", "system energy usage")
    ]
    triz_matrix = load_triz_matrix("data/mock_triz_matrix.json")
    results = bind_all_conflicts(mock_pairs, triz_matrix)

    for r in results:
        print(f"{r['attribute_a']} vs {r['attribute_b']}")
        for pid, name in r['principles']:
            print(f"  - [{pid}] {name}")
        print()

if __name__ == "__main__":
    demo()
