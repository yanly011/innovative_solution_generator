import streamlit as st
from story_generator import generate_innovation_record

st.set_page_config(page_title="TRIZ Innovation Generator", layout="wide")

st.title("TRIZ Innovation Generator")
st.markdown("Enter a system scene, two conflicting attributes, and a TRIZ principle to generate a structured innovation scenario.")

scene = st.text_area("System Scene", height=100, value="A fully automated smart kitchen in a fast-food restaurant.")

attribute_a = st.text_input("Attribute A (to be improved)", value="cooking speed")
general_param_a = st.text_input("General Parameter A", value="speed")

attribute_b = st.text_input("Attribute B (potentially in conflict)", value="temperature consistency")
general_param_b = st.text_input("General Parameter B", value="temperature")

triz_options = {
    15: "Dynamics",
    10: "Preliminary Action",
    13: "The Other Way Around",
    3: "Local Quality",
    25: "Self-service"
}
principle_id = st.selectbox("Select TRIZ Principle", options=list(triz_options.keys()))
principle_name = triz_options[principle_id]

if st.button("Generate Innovation Scenario"):
    with st.spinner("Generating..."):
        result = generate_innovation_record(
            scene=scene,
            attribute_a=attribute_a,
            attribute_b=attribute_b,
            general_param_a=general_param_a,
            general_param_b=general_param_b,
            principle=(principle_id, principle_name)
        )

    st.subheader("Input Summary")
    st.json({
        "Scene": result["scene"],
        "Attribute A": f'{result["attribute_a"]} → {result["general_param_a"]}',
        "Attribute B": f'{result["attribute_b"]} → {result["general_param_b"]}',
        "TRIZ Principle": f'[{result["triz_principle"][0]}] {result["triz_principle"][1]}'
    })

    st.subheader("Generated Innovation Scenario")
    st.markdown(result["story"])