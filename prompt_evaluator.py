from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Passo 1 — pedir o prompt
prompt = input("Enter your prompt: ")

# Passo 2 — mandar para a OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Passo 3 — mostrar a resposta
answer = response.choices[0].message.content
print(f"\nAI Response:\n{answer}")

# Passo 4 — pedir o score
score = int(input("\nEnter your score (1-10): "))

# Passo 5 — criar o resultado
result = {
    "prompt": prompt,
    "response": answer,
    "score": score
}

# Passo 6 — ler arquivo existente ou criar lista vazia
try:
    with open("results.json", "r") as f:
        data = json.load(f)
        if not isinstance(data, list):
            data = []
except:
    data = []

# Passo 7 — adicionar novo resultado
data.append(result)

# Passo 8 — salvar tudo de volta
with open("results.json", "w") as f:
    json.dump(data, f, indent=2)

print(f"\nResult saved. Total evaluations: {len(data)}")