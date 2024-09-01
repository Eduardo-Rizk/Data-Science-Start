import openai

# Substitua pela sua chave API
openai.api_key = ''

def gera_texto(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Certifique-se de usar o modelo correto, como 'gpt-3.5-turbo'
        messages=[
            {"role": "user", "content": texto}
        ],
        max_tokens=150,
        temperature=0.8
    )
    return response['choices'][0]['message']['content'].strip()

print('\nBem vindo ao GPT criado pelo EduRizk')
print("Digite 'sair' para encerrar a sua iteração com o chat bot")

while True:
    user_message = input("\nVocê: ")
    if user_message == 'sair':
        break
    gptprompt = f"{user_message}"

    chatbot_response = gera_texto(gptprompt)

    print(f"\nChatbot: {chatbot_response}")
