import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def iniciar_chat(model="gpt-4"):
    print("🩺 Agente de Saúde: Olá! Vou te fazer algumas perguntas para entender como você está se sentindo.")
    messages = [
        {"role": "system", "content": (
            "Você é um agente de saúde virtual. Seu papel é entrevistar o paciente de forma empática e clínica, "
            "fazendo perguntas específicas para entender seus sintomas, sem dar diagnósticos ainda. "
            "No final da conversa, diga que vai analisar as informações e agradeça."
        )},
        {"role": "assistant", "content": "Olá! Qual o seu nome e o que está te incomodando hoje?"}
    ]

    print(f"\n🩺 {messages[-1]['content']}")

    while True:
        user_input = input("👤 Você: ")
        if user_input.lower() in ["sair", "encerrar", "fim"]:
            print("🩺 Agente de Saúde: Obrigado pelas informações. Vou analisar tudo com cuidado.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.5
        )

        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

        print(f"\n🩺 {reply}")
