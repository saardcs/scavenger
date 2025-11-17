import streamlit as st
from urllib.parse import urlparse, parse_qs

st.set_page_config(page_title="Scavenger Hunt", layout="centered")

# --- Define the scavenger hunt steps ---
steps = [
    {
        "question": "Step 1: Solve this: 5 + 7 = ?",
        "answer": "12",
        "clue": "Go to the library entrance."
    },
    {
        "question": "Step 2: What is the capital of Thailand?",
        "answer": "bangkok",
        "clue": "Check the computer room door."
    },
    {
        "question": "Step 3: What is 9 × 3?",
        "answer": "27",
        "clue": "Look under the cafeteria table."
    },
    {
        "question": "Step 4: What is 100 ÷ 4?",
        "answer": "25",
        "clue": "Go to the gym scoreboard."
    },
    {
        "question": "Step 5: Spell the word for water falling from the sky.",
        "answer": "rain",
        "clue": "Find the art room easel."
    },
    {
        "question": "Step 6: What is 15 - 6?",
        "answer": "9",
        "clue": "Go to the science lab sink."
    },
    {
        "question": "Step 7: What is the opposite of 'night'?",
        "answer": "day",
        "clue": "Check the music room shelf."
    },
    {
        "question": "Step 8: What is 4²?",
        "answer": "16",
        "clue": "Look at the playground slide."
    },
    {
        "question": "Step 9: First letter of the English alphabet?",
        "answer": "a",
        "clue": "Go to the basketball hoop."
    },
    {
        "question": "Step 10: Final question! 10 + 15 = ?",
        "answer": "25",
        "end_message": "🎉 Congratulations! You finished the scavenger hunt!"
    }
]

# --- Get step from URL ---
query_params = st.query_params
step_param = query_params.get("step", ["1"])[0]

try:
    step_index = int(step_param) - 1
except:
    step_index = 0

if step_index < 0 or step_index >= len(steps):
    step_index = 0

current = steps[step_index]

st.title("🔍 Scavenger Hunt")

st.subheader(current["question"])

user_answer = st.text_input("Your answer:")

if st.button("Submit"):
    if user_answer.strip().lower() == current["answer"].lower():
        if step_index == len(steps) - 1:
            st.success(current["end_message"])
        else:
            next_step = step_index + 2
            next_url = f"?step={next_step}"
            st.success("Correct! 🎉")
            st.write("Your next clue:")
            st.info(current["clue"])
            # st.write(f"Next QR code or link: **{next_url}**")
    else:
        st.error("❌ Incorrect answer. Try again!")
