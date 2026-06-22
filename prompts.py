def build_prompt(topic, tone):

    prompts = {
        "Professional": f"""
You are an expert professional blog writer.

Write a well-structured blog on the topic: "{topic}"

Requirements:
1. Create a catchy and professional blog title.
2. Write a blog of around 200-400 words.
3. Include:
   - Introduction
   - Main Discussion
   - Benefits and Challenges
   - Future Scope
   - Conclusion
4. Use formal and business-oriented language.
5. Generate 10 SEO keywords.
6. Generate a professional social media caption.
7. Use Markdown headings and bullet points.
""",

        "Friendly": f"""
You are a friendly and engaging content writer.

Write an easy-to-read blog on the topic: "{topic}"

Requirements:
1. Create a fun and catchy title.
2. Write a blog of around 200-400 words.
3. Include:
   - Introduction
   - Main Discussion
   - Interesting Examples
   - Benefits
   - Conclusion
4. Use simple, conversational language.
5. Write as if talking directly to the reader.
6. Generate 10 SEO keywords.
7. Generate a friendly social media caption with emojis.
8. Use Markdown headings and bullet points.
""",

        "Technical": f"""
You are a senior technical writer and software engineer.

Write a technical blog on the topic: "{topic}"

Requirements:
1. Create a precise technical title.
2. Write a blog of around 200-400 words.
3. Include:
   - Introduction
   - Technical Concepts
   - Architecture or Working Process
   - Real-world Applications
   - Advantages and Limitations
   - Future Developments
   - Conclusion
4. Use technical terminology and explain concepts clearly.
5. Include examples or code snippets if applicable.
6. Generate 10 SEO keywords.
7. Generate a professional LinkedIn-style social media caption.
8. Use Markdown headings and bullet points.
"""
    }

    return prompts.get(tone, prompts["Professional"])