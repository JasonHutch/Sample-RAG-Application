from flask import Flask, request, Response
from tasks.FlashCardGeneration import GenerateFlashCards

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/generateCards")
def generate_cards():
    try:
        query = request.args.get('q')
        print(f"Query is {query}")

        if (query is not None):
            flash_cards = GenerateFlashCards(query,'Microservices_Patterns.pdf')
        else:
            flash_cards = "Please add ?query=<Your query> to generate flash cards"

        return flash_cards
    
    except Exception as e:
        return f"Internal Server Error womp womp{e}"