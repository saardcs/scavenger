import streamlit as st

st.set_page_config(
    page_title="Secure Scavenger Hunt",
    layout="centered"
)

# --- Load data from secrets ---
steps = st.secrets["scavenger_hunt"]["steps"]
tokens = st.secrets["scavenger_hunt"]["tokens"]
images = st.secrets["scavenger_hunt"]["images"]

# --- Map token -> page index ---
token_map = {token: idx for idx, token in enumerate(tokens)}

# --- Read token from URL ---
token = st.query_params.get("token", [""])[0]

# --- Find matching page ---
step_index = token_map.get(token)

st.title("🔐 Scavenger Hunt")

# --- Invalid token ---
if step_index is None:
    st.error("Invalid or missing token.")
    st.stop()

# --- Get current step ---
current = steps[step_index]

# --- Show image ---
if step_index < len(images):
    st.image(images[step_index], use_container_width=True)

# --- Show question/text ---
st.subheader(current["question"])
