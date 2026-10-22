"""Esempio base LangChain: prompt + modello + parser (LCEL)."""

import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit(
        "Manca OPENAI_API_KEY. Copia .env.example in .env e inserisci la chiave."
    )

model = init_chat_model("openai:gpt-4o-mini", temperature=0.3)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Sei un assistente conciso. Rispondi in italiano."),
        ("human", "{question}"),
    ]
)

chain = prompt | model | StrOutputParser()


def main() -> None:
    question = "Cos'è LangChain in due frasi?"
    print(f"> {question}\n")
    print(chain.invoke({"question": question}))


if __name__ == "__main__":
    main()
