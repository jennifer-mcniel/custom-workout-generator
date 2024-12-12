
from groq import Groq

api_key = "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"

client = Groq(
    api_key=api_key,
)

def getTestLLMMessage():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Explain the importance of fast language models",
            }
        ],
        model="llama3-8b-8192"
    )

    return chat_completion.choices[0].message.content

def generate_response(messages, model="llama-3.1-8b-instant", max_tokens=6000, temperature=0.9):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        max_tokens=max_tokens,
        temperature=temperature
    )

    response = chat_completion.choices[0].message.content
    return response

def create_message(prompt):
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]

    return messages