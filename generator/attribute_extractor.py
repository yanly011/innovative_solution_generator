import openai

# You need to set your API key before using
# openai.api_key = "YOUR_API_KEY"

# Prompt template for extracting engineering-relevant attributes
def build_prompt(scene_description: str) -> str:
    return f"""
You are an AI assistant with expertise in systems thinking, TRIZ, and engineering design.

Given the following real-world system scenario:
"""
{scene_description}
"""

List 8 to 12 relevant system or service attributes that can be mapped to general engineering parameters. Each attribute should be:
- Concise (2–4 words)
- Expressed as measurable or controllable properties (e.g., response time, material strength, user error rate)
- Neutral in direction (don't assume good or bad)

Output a Python list of strings. Do not explain.
"""

# Call the OpenAI API to extract attributes from a scene
def extract_attributes(scene: str, model="gpt-4"):
    prompt = build_prompt(scene)

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    result_text = response["choices"][0]["message"]["content"]

    try:
        # Evaluate the response safely as a list
        attributes = eval(result_text.strip())
        if isinstance(attributes, list):
            return [a.strip() for a in attributes if isinstance(a, str)]
        else:
            return []
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw response was:", result_text)
        return []

# Example usage
if __name__ == "__main__":
    test_scene = "A fully automated smart kitchen in a fast-food restaurant, responsible for cooking, packaging, and handing over meals via robot arms."
    attributes = extract_attributes(test_scene)
    print("Extracted Attributes:")
    for i, attr in enumerate(attributes):
        print(f"{i+1}. {attr}")
