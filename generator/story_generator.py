import openai
from typing import List, Tuple, Dict

# You need to set your OpenAI API key before running
# openai.api_key = "YOUR_API_KEY"

# Build prompt from attributes + TRIZ principle + scene
def build_story_prompt(scene: str, attribute_a: str, attribute_b: str,
                        general_param_a: str, general_param_b: str,
                        principle: Tuple[int, str]) -> str:
    return f"""
You are an expert innovation strategist and TRIZ practitioner.

Given the following input:

- System Scene: {scene}
- Attribute A: {attribute_a} → General Parameter: {general_param_a}
- Attribute B: {attribute_b} → General Parameter: {general_param_b}
- TRIZ Principle: [{principle[0]}] {principle[1]}

Please generate a detailed, imaginative, and plausible innovation concept based on applying the TRIZ principle to resolve the conflict between A and B.

Your response must include:
- A fictional but realistic system context
- How the conflict manifests in this system
- How the TRIZ principle is applied creatively
- A description of the resulting system behavior or architecture
- Emphasis on novel, surprising, or counterintuitive aspects

Do NOT provide a list. Write a single detailed paragraph as a scenario.
"""

def generate_innovation_record(scene: str, attribute_a: str, attribute_b: str,
                                general_param_a: str, general_param_b: str,
                                principle: Tuple[int, str], model="gpt-4") -> Dict:
    prompt = build_story_prompt(scene, attribute_a, attribute_b,
                                 general_param_a, general_param_b,
                                 principle)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=500
    )

    story = response["choices"][0]["message"]["content"].strip()

    return {
        "scene": scene,
        "attribute_a": attribute_a,
        "attribute_b": attribute_b,
        "general_param_a": general_param_a,
        "general_param_b": general_param_b,
        "triz_principle": [principle[0], principle[1]],
        "story": story
    }

# Example usage
def demo():
    scene = "A fully automated smart kitchen in a fast-food restaurant."
    attribute_a = "cooking speed"
    attribute_b = "temperature consistency"
    general_param_a = "speed"
    general_param_b = "temperature"
    principle = (15, "Dynamics")

    record = generate_innovation_record(scene, attribute_a, attribute_b,
                                        general_param_a, general_param_b,
                                        principle)
    print("Generated Innovation Record:\n")
    for k, v in record.items():
        if k != "story":
            print(f"{k}: {v}")
    print("\nStory:\n" + record["story"])

if __name__ == "__main__":
    demo()
