# Generative Innovation Lab

A modular AI-powered innovation system that combines TRIZ principles, engineering abstraction, and large language models (LLMs) to generate creative solution concepts in response to system-level contradictions.

## 🚀 Project Overview

This project aims to explore the generative capabilities of LLMs (like GPT-4) in producing plausible and unconventional innovation scenarios based on abstract engineering contradictions. It is loosely inspired by the TRIZ methodology but emphasizes automatic attribute abstraction, combinatorial conflict synthesis, and free-form concept generation.

## ✨ Key Features

- **Attribute Extraction**: Convert system scene descriptions into abstract engineering parameters
- **Conflict Enumeration**: Generate all possible two-way parameter contradictions
- **TRIZ Principle Binding**: Match parameter pairs to TRIZ inventive principles using keyword heuristics
- **Innovation Story Generator**: Produce detailed, scenario-based solution stories using LLMs
- **Streamlit Web App**: Interactive user interface for input, exploration, and generation

## 📦 Directory Structure

```
generative_innovation_lab/
├── generator/
│   ├── attribute_extractor.py      # Scene → abstract parameters
│   ├── conflict_enumerator.py      # Enumerate parameter pairs
│   ├── triz_binder.py              # Match principles to parameter pairs
│   ├── story_generator.py          # Generate solution stories with LLM
│   └── utils.py                    # (optional) shared tools
├── data/
│   └── triz_matrix.json            # Mapping of keywords to TRIZ principles
├── prompts/
│   └── story_prompt_template.txt   # Prompt examples (optional)
├── app.py                          # Streamlit app interface
├── run_demo.py                     # Script-based batch generation (optional)
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation
```

## 🧪 Example Use Case

**Input:**
- Scene: "A fully automated smart kitchen in a fast-food restaurant."
- Attribute A: "cooking speed" → General Parameter: "speed"
- Attribute B: "temperature consistency" → General Parameter: "temperature"
- TRIZ Principle: [15] Dynamics

**Output:**
A paragraph describing a novel system behavior that applies TRIZ Principle 15 to resolve a contradiction between speed and temperature in a futuristic kitchen scenario.

## 🔧 Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the web app
streamlit run app.py
```

## 🧠 Future Work
- Semantic similarity-based principle binding
- Rating and filtering for quality control
- Visualization of TRIZ matrix traversal
- Export of generated innovations in JSONL format for dataset creation

## 📜 License
MIT License (or specify yours here)

---
Created with curiosity and creativity.
