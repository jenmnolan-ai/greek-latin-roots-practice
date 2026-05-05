import streamlit as st
import random

st.set_page_config(page_title="Greek & Latin Roots Practice")

st.title("🌱 Greek & Latin Roots Practice")

st.write("Practice root words a little at a time. Focus on patterns: root + 'ology' = study of.")

# --- WORD LIST ---
words = [
    {
        "word": "biology",
        "root": "bio = life, ology = study of",
        "question": "What does biology mean?",
        "options": ["Study of life", "Study of earth", "Study of stars"],
        "answer": "Study of life",
        "explanation": "Bio = life → biology = study of life."
    },
    {
        "word": "exobiology",
        "root": "exo = outside, bio = life",
        "question": "What does exobiology mean?",
        "options": ["Study of animals", "Study of life outside Earth", "Study of causes"],
        "answer": "Study of life outside Earth",
        "explanation": "Exo = outside → life outside Earth."
    },
    {
        "word": "ecology",
        "root": "eco = environment",
        "question": "What does ecology mean?",
        "options": ["Study of the environment", "Study of time", "Study of stars"],
        "answer": "Study of the environment",
        "explanation": "Eco = environment → study of interactions in the environment."
    },
    {
        "word": "etiology",
        "root": "etio = cause",
        "question": "What does etiology mean?",
        "options": ["Study of causes", "Study of animals", "Study of sound"],
        "answer": "Study of causes",
        "explanation": "Etio = cause → study of causes."
    },
    {
        "word": "geology",
        "root": "geo = earth",
        "question": "What does geology mean?",
        "options": ["Study of earth", "Study of stars", "Study of family"],
        "answer": "Study of earth",
        "explanation": "Geo = earth → study of earth."
    },
    {
        "word": "astrology",
        "root": "astro = star",
        "question": "What does astrology study?",
        "options": ["Stars and their influence", "Animals", "Time"],
        "answer": "Stars and their influence",
        "explanation": "Astro = star → study of stars and influence."
    },
    {
        "word": "genealogy",
        "root": "genea = family",
        "question": "What does genealogy mean?",
        "options": ["Study of family history", "Study of sound", "Study of earth"],
        "answer": "Study of family history",
        "explanation": "Genea = family → family history."
    },
    {
        "word": "zoology",
        "root": "zoo = animal",
        "question": "What does zoology mean?",
        "options": ["Study of animals", "Study of time", "Study of stars"],
        "answer": "Study of animals",
        "explanation": "Zoo = animal → study of animals."
    },
    {
        "word": "chronology",
        "root": "chron = time",
        "question": "What does chronology mean?",
        "options": ["Study of time/order of events", "Study of life", "Study of sound"],
        "answer": "Study of time/order of events",
        "explanation": "Chron = time → ordering events in time."
    },
    {
        "word": "psychology",
        "root": "psych = mind",
        "question": "What does psychology mean?",
        "options": ["Study of the mind", "Study of animals", "Study of stars"],
        "answer": "Study of the mind",
        "explanation": "Psych = mind → study of the mind."
    },
    {
        "word": "cosmology",
        "root": "cosm = universe",
        "question": "What does cosmology mean?",
        "options": ["Study of the universe", "Study of sound", "Study of causes"],
        "answer": "Study of the universe",
        "explanation": "Cosm = universe → origin and development of the universe."
    },
    {
        "word": "audiology",
        "root": "audi = hearing",
        "question": "What does audiology mean?",
        "options": ["Study of hearing", "Study of animals", "Study of time"],
        "answer": "Study of hearing",
        "explanation": "Audi = hearing → study of hearing."
    },
    {
        "word": "ethnology",
        "root": "ethn = people/race",
        "question": "What does ethnology mean?",
        "options": ["Study of people and cultures", "Study of stars", "Study of earth"],
        "answer": "Study of people and cultures",
        "explanation": "Ethn = people → study of different groups."
    },
    {
        "word": "anthropology",
        "root": "anthrop = human",
        "question": "What does anthropology mean?",
        "options": ["Study of humans", "Study of sound", "Study of animals"],
        "answer": "Study of humans",
        "explanation": "Anthrop = human → study of humans."
    },
    {
        "word": "paleoanthropology",
        "root": "paleo = ancient, anthrop = human",
        "question": "What does paleoanthropology mean?",
        "options": ["Study of ancient humans", "Study of animals", "Study of time"],
        "answer": "Study of ancient humans",
        "explanation": "Paleo = ancient → ancient humans."
    }
]

# --- SESSION STATE ---
if "current" not in st.session_state:
    st.session_state.current = random.choice(words)

card = st.session_state.current

# --- DISPLAY ---
st.subheader(f"Word: {card['word']}")

st.info(card["root"])

choice = st.radio(card["question"], card["options"])

if st.button("Check Answer"):
    if choice == card["answer"]:
        st.success("Correct! Nice work.")
    else:
        st.error("Not quite. Look at the root clue again.")
    st.write(card["explanation"])

if st.button("Next Word"):
    st.session_state.current = random.choice(words)
    st.rerun()
