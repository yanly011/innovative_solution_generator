from prompt_builder.builder import generate_prompt

if __name__ == "__main__":
    # Example input
    principle_id = 10
    principle_name = "Pre-action"
    contradiction = ("System Reliability", "System Complexity")
    industry = "Smart Furniture"
    num_cases = 2

    # Generate Prompt
    prompt_text = generate_prompt(
        principle_id=principle_id,
        principle_name=principle_name,
        contradiction=contradiction,
        industry=industry,
        num_cases=num_cases
    )

    print("===== Generated Prompt Text =====")
    print(prompt_text)