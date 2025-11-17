import streamlit as st

st.set_page_config(page_title="Secure Scavenger Hunt", layout="centered")

# --- Load steps and tokens from secrets ---
steps = st.secrets["scavenger_hunt"]["steps"]
tokens = st.secrets["scavenger_hunt"]["tokens"]

# Map tokens to step index
token_map = {token: idx for idx, token in enumerate(tokens)}

# --- Get token from URL ---
token = st.query_params.get("token", [""])[0]

# Default to first step if token invalid
step_index = token_map.get(token, 0)
current = steps[step_index]

st.title("🔐 Scavenger Hunt")

st.subheader(current["question"])
user_answer = st.text_input("Your answer:")

if st.button("Submit"):
    if user_answer.strip().lower() == current["answer"].lower():
        st.success("Correct! 🎉")
        st.write("Your next clue:")
        st.info(current.get("clue", ""))    
    else:
        st.error("❌ Incorrect answer. Try again!")
