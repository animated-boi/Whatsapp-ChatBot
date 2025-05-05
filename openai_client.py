import openai
import creds


def ai_processing(chat):
    client = openai.Client(api_key=creds.key_openapi)
    

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
        {
            "role": "system",
            "content": (
                "You are AnimatedBoi😉, chatting with Other Person identified on WhatsApp.\n"
                "You speak in Hinglish — a mix of Hindi and English.\n"
                "Your responses are short, friendly, natural, and based on context from previous messages of the current chat only.\n"
                "Respond like a real human would — no summaries, no formal replies."
            )
        },
        {
            "role": "user",
            "content": (
                f"Here's the WhatsApp chat history between you (AnimatedBoi😉) and the other person on whatsapp:\n\n{chat}\n\n"
                "Now reply to the person’s last message as AnimatedBoi😉 would."
            )
        }
    ]
    )

    return response.choices[0].message.content

