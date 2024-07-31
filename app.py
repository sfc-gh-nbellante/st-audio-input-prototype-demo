import streamlit as st


audio = st.audio_input(label="todo")

if audio:
    st.audio(audio.getbytes())
