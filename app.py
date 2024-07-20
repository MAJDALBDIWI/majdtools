from flask import Flask, request, jsonify
import libretranslate

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate_text():
    text = request.form["text"]
    target_language = request.form["target_language"]

    translator = libretranslate.Translator()
    translation = translator.translate(text, "de", target_language)

    return jsonify({"translation": translation})

if __name__ == "__main__":
    app.run(debug=True)
