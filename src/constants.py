CHROMA_PATH='chroma'
OPEN_AI_API_KEY='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'
FLASH_CARD_PROMPT_TEMPLATE = """

Create 20 flash cards based on the following context:

{context}

---

Create flash cards in a question anwser format based on the above context that helps a user better understand:{question} these responses should be formatted in json.
"""