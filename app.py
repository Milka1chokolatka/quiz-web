from flask import Flask, render_template, request
from db.crud import get_quizes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        quizes = get_quizes()
        return render_template("index.html", quizes_list=quizes)
    else:
        quiz_id = request.form.get("quiz")
        print(quiz_id)
        return f"Вікторина {quiz_id}"

@app.route("/test")
def test():
    return "<h1> Тестування </h1>"

@app.route("/result")
def result():
    return "<h1> Смерть </h1>"



if __name__ == "__main__":
    app.run()