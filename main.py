from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("dictionary.csv")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>/")
def api(word):
    provided_word = word.lower()
    for index, word in enumerate(df.word):
        if provided_word == word:
            word_index = index
            word_definition = df.definition[word_index]

            result_dictionary = {"word": word.title(), "definition": word_definition.strip()}
            return result_dictionary


if __name__ == "__main__":
    app.run(debug=True)
