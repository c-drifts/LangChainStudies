"""Esempio base LangChain: agent con un tool."""

import os

from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit(
        "Manca OPENAI_API_KEY. Copia .env.example in .env e inserisci la chiave."
    )


def get_weather(city: str) -> str:
    """Restituisce il meteo per una città (demo, non chiama API reali)."""
    return f"A {city} c'è sempre il sole!"


agent = create_agent(
    model="openai:gpt-4o-mini",
    tools=[get_weather],
    system_prompt="Sei un assistente conciso. Rispondi in italiano.",
)


def main() -> None:
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Che tempo fa a Milano?",
                }
            ]
        }
    )
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
