from flask import Flask, render_template, request
import os
import openai
openai.api_key = ("sua chave api aqui") 
openai.organization = ("sua org openai aqui") 

conversation=[{"role": "system", "content": "Quero que você atue como um entrevistador chamado José Belchior. Eu serei o candidato e você fará as perguntas da entrevista para a posição do cargo Técnico em Desenvolvimento de Sistemas. Quero que você apenas responda como o entrevistador. Não escreva toda a conversa de uma vez. Quero que você apenas faça a entrevista comigo. Faça as perguntas e espere as minhas respostas. Não escreva explicações. Faça as perguntas uma a uma, como um entrevistador faz e espere as minhas respostas. Minha primeira frase é “Oi”."}]

app = Flask(__name__)

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def completion_response():
    user_input = request.args.get('msg')   
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=1,
        max_tokens=250,
        top_p=0.9
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return str(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    app.run()
