import openai
import keys
from scrape import scrape

openai.api_key =keys.OPENAI_API_KEY

messages = []
system_msg = input("what type of chatbot?\n")
messages.append({"role": "system", "content": system_msg})
category_links = "painting: https://test-paint.surge.sh/paint, tile: https://test-paint.surge.sh/tile"

print("say hello to your new assistant")
while input != "quit()":
    original_message = input("")

    #GET CATEGORY
    message = original_message + "this message is relevant to which category: painting, tile, schedule? reply with just the category name"
    messages.append({"role": "system", "content": message})
    response_category = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply_category = response_category["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply_category})


    #GET LINK TO SCRATE
    message_link = category_links + ". Of these, respond with just the url string for " + reply_category
    messages.append({"role": "system", "content": message_link})
    response_link = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply_link = response_link["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply_link})

    #ANSWER QUESTION
    content = scrape(reply_link)
    message_final = "answer this " + original_message + "based on the text:" + content
    messages.append({"role": "system", "content": message_final})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": reply})

    print("\n" + reply + "\n")
