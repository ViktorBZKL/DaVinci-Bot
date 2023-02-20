import openai
import telebot



while True:
    openai.api_key = False
    token = False
    openai.api_key = input("Enter OpenAI API: ")
    token = input("Enter TelegramBot API: ")
    if openai.api_key != "" and token != "":
        print("Great! If API is right then your bot is working")
        break

bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])

bot.polling()