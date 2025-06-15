from generator.story_generator import generate_innovation_record

# Example list of input records (each record is a 3-tuple with scene, attributes, and principle)
demo_records = [
    {
        "scene": "A fully automated smart kitchen in a fast-food restaurant.",
        "attribute_a": "cooking speed",
        "attribute_b": "temperature consistency",
        "general_param_a": "speed",
        "general_param_b": "temperature",
        "principle": (15, "Dynamics")
    },
    {
        "scene": "A drone-based parcel delivery system in an urban environment.",
        "attribute_a": "delivery speed",
        "attribute_b": "energy consumption",
        "general_param_a": "speed",
        "general_param_b": "energy",
        "principle": (25, "Self-service")
    },
    {
        "scene": "A smart classroom using AI teaching assistants.",
        "attribute_a": "student engagement",
        "attribute_b": "teacher workload",
        "general_param_a": "usability",
        "general_param_b": "cost",
        "principle": (3, "Local Quality")
    }
]

# Generate and display results in batch
def run_batch(records):
    for i, item in enumerate(records):
        print("=" * 80)
        print(f"Innovation Scenario #{i+1}")
        result = generate_innovation_record(
            scene=item["scene"],
            attribute_a=item["attribute_a"],
            attribute_b=item["attribute_b"],
            general_param_a=item["general_param_a"],
            general_param_b=item["general_param_b"],
            principle=item["principle"]
        )

        print(f"Scene: {result['scene']}")
        print(f"A: {result['attribute_a']} → {result['general_param_a']}")
        print(f"B: {result['attribute_b']} → {result['general_param_b']}")
        print(f"TRIZ: [{result['triz_principle'][0]}] {result['triz_principle'][1]}")
        print("\nStory:")
        print(result['story'])
        print("\n")

if __name__ == "__main__":
    run_batch(demo_records)
