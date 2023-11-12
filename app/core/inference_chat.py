from .setup_bot import chain as LLMChain

def ask_llm(question:str):
    output = LLMChain.invoke(input=question).strip()
    return output