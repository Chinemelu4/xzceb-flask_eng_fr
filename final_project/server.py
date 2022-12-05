import machinetranslation
from machinetranslation import translator
from translator import english_to_french, french_to_english
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=['POST','GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    t=english_to_french(textToTranslate)
    return render_template('index.html',"Translated text to French",t)

@app.route("/frenchToEnglish", methods=['POST','GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

    return render_template('index.html')

if  __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)
