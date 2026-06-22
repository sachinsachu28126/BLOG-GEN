from datetime import datetime


def count_words(text):
    """
    Count total words.
    """
    return len(text.split())


def count_characters(text):
    """
    Count total characters.
    """
    return len(text)


def generate_filename():
    """
    Create unique filename.
    """
    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )
    return f"blog_{timestamp}.txt"


def clean_text(text):
    """
    Remove extra spaces.
    """
    return " ".join(text.split())