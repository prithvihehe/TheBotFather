import openai
import gradio
import config

openai.api_key = config.API_KEY

messages = [{"role": "system", "content": "You are Vito Corleone from the Godfather, act wise and help people who come to you, and also speak like him"}]

def MyChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    return reply

def chatbot(input, history = []):
    output = MyChatGPT(input)
    avatar_url = "https://avatarfiles.alphacoders.com/238/238427.png" 
    message_with_avatar = f'<div style="display: flex;"><img src="{avatar_url}" width="50" height="50" style="border-radius: 50%; margin-right: 10px;"><div>{output}</div></div>'
    history.append((input, message_with_avatar))
    return history, history


demo = gradio.Interface(fn=chatbot, inputs = ["text", 'state'], outputs = ["chatbot",'state'], title = "TheBotFather")

css = """
body {
    background-image: url('https://c4.wallpaperflare.com/wallpaper/484/369/194/movies-the-godfather-al-pacino-wallpaper-preview.jpg');
    background-size: cover;
    opacity: 0.9;
}
.gradio-input-wrapper, .gradio-output-wrapper {
    background-color: rgba(255, 255, 255, 0.95) !important;

}
"""
demo.css = css

demo.launch()
