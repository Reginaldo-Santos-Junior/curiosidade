import streamlit as st
import requests

api_key = st.secrets["chave_api"]["api_key"]

def generate_text(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"}
        ]
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    response_json = response.json()
    return response_json["choices"][0]["message"]["content"] if "choices" in response_json else ""

def main():
    st.title("Aplicação para curiosidades aleatorias!")

    # Cria um campo de entrada de texto para o prompt
    prompt = "Me fale uma curiosidade aleatoria interessante"

    # Quando o botão for pressionado, gera o texto e exibe na interface
    if st.button("Quero aprender algo novo 🕵️‍♂️"):
        generated_response = generate_text(prompt)
        st.text("Curiosidade 👇:")
        st.write(generated_response)

if __name__ == "__main__":
    main()
