from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

llm=OllamaLLM(
    model='llama3.2',
    base_url='http://localhost:11434',
    temperature=0.6
)

def generate_restaurant(cuisine):

    prompt_name=PromptTemplate(
        input_variables=['cuisine'],
        template='I want to open a restaurant for {cuisine} food. Suggest a fancy name for this. Don\'t provide any context with it only provide one name ',
    )
    prompt_menu=PromptTemplate(
        input_variables=['res_name'],
        template='List 8 menu items for "{res_name}" as comma-separated values only. No extra text.'
    )


    name_chain= prompt_name | llm | StrOutputParser()
    menu_chain= prompt_menu | llm | StrOutputParser()

    chain = (
        RunnablePassthrough.assign(
            res_name=name_chain
        )
        | RunnablePassthrough.assign(
            res_menu = lambda x: menu_chain.invoke(
                {'res_name': x['res_name']}
            )
        )
    )

    output = chain.invoke({'cuisine':cuisine})

    return output

