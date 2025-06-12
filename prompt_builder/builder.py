def generate_prompt(principle_id, principle_name, contradiction, industry, num_cases=2):
    contradiction_str = f"{contradiction[0]} vs. {contradiction[1]}"
    prompt = f"""You are an expert in innovation design and TRIZ methodology.

Your task is to generate {num_cases} hypothetical but plausible innovation solutions based on the following inputs:

- TRIZ Principle #{principle_id}: {principle_name}
  > [Insert explanation here if needed]

- Technical Contradiction:
  > {contradiction_str}

- Industry/Application Context: {industry}

For each solution, please provide:

1. Solution Name
2. Short Description
3. How it reflects the TRIZ Principle
4. How it addresses the contradiction
5. Expected Value

Make sure the generated innovations are technically reasonable and situated in the given context."""
    return prompt
