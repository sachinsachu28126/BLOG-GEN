def build_prompt(topic, tone):

    prompt = f"""
    You are an expert blog writer.

    Topic:
    {topic}

    Tone:
    {tone}

    Generate:

    1. Blog Title
    2. Detailed Blog Content
       - Introduction
       - Main Concepts
       - Examples
       - Benefits
       - Challenges
       - Future Scope
       - Conclusion

    3. 15 SEO Keywords
    4. Social Media Caption
    5. Call To Action

    Write professionally and in markdown format.
    """

    return prompt