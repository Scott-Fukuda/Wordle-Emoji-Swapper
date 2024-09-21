from flask import Flask,render_template,request, jsonify
# request is a module that enables us to pull data from "form" in website.html
import pyperclip
import functions
import random

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('website.html')

@app.route("/results", methods = ['POST'])
def results():
    output = request.form.to_dict()
    user_score = output["user_score"] # this is something called a python dictionary
    toggleSwitch = output["toggle"]
    green = output["green"]
    yellow = output["yellow"]
    grey = output["grey"]
    if toggleSwitch:
        (green, yellow, grey) = random.sample(functions.emoji_list, 3)
    new_user_score = functions.emoji_swap(green, yellow, grey, user_score)
    # new_user_score = user_score
    return render_template("website.html", new_user_score=new_user_score)

@app.route('/copy', methods=['POST'])
def copy():
    data = request.json
    text_to_copy = data.get('text')
    pyperclip.copy(text_to_copy)
    return jsonify({'status': 'success', 'message': 'Text copied to clipboard!'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
