from src.db.db_util import GetContextFromDb
from src.constants import OPEN_AI_API_KEY, FLASH_CARD_PROMPT_TEMPLATE
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def GenerateFlashCards(user_query, file_name):
    context_text = GetContextFromDb(file_name, user_query)

    prompt_template = ChatPromptTemplate.from_template(FLASH_CARD_PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=user_query)

    model = ChatOpenAI(api_key=OPEN_AI_API_KEY)
    return model.predict(prompt)
