import streamlit as st
from services import generate_blog
from utils import (
    count_words,
    count_characters,
    generate_filename
)

st.set_page_config(
    page_title="AI Blog Content Generator",
    page_icon="✍️",
    layout="wide"
)

st.title("✍️ AI Blog Content Generator")

topic = st.text_input(
    "Enter Blog Topic"
)

tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Technical"
    ]
)

if st.button(
    "Generate Blog"
):

    if not topic:
        st.warning(
            "Please enter a topic."
        )

    else:
        with st.spinner(
            "Generating Blog..."
        ):

            result = generate_blog(
                topic,
                tone
            )

        st.success(
            "Blog Generated Successfully!"
        )

        st.markdown(result)

        st.info(
            f"Words: {count_words(result)}"
        )

        st.info(
            f"Characters: {count_characters(result)}"
        )

        st.download_button(
            "Download Blog",
            data=result,
            file_name=generate_filename(),
            mime="text/plain"
        )