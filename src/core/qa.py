def get_response(client, messages, model):
    response = client.chat.completions.create(
        messages = messages,
        model = model,
    )

    return response.choices[0].message.content
    