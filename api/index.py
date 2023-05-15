from flask import Flask, request, jsonify
from gpt4free import you

app = Flask(__name__)

@app.route("/create_completion", methods=["POST"])
def create_completion():
    data = request.json
    prompt = data['prompt']
    detailed = data.get('detailed', False)
    include_links = data.get('include_links', False)
    chat = data.get('chat', [])

    response = you.Completion.create(
        prompt=prompt,
        detailed=detailed,
        include_links=include_links,
        chat=chat)

    return jsonify(response.dict())

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    prompt = data['prompt']
    chat = data.get('chat', [])

    response = you.Completion.create(
        prompt=prompt,
        chat=chat)

    return jsonify({"bot_response": response.text})