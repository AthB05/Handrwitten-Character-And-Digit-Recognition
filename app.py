import numpy as np
from flask import (Flask, render_template, request,redirect, url_for, session)
from tensorflow import keras

LABELS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'd', 'e', 'f', 'g', 'h', 'n', 'q', 'r', 't']

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def rec():
    pixels = request.form['pixels']
    pixels = pixels.split(',')
    img = np.array(pixels).astype(float).reshape(1, 784)
    model = keras.models.load_model('model\model.h5')
    pred_letter = model.predict(img)
    letter = str(LABELS[np.argmax(pred_letter)])
    print(letter)
    return render_template("index.html", letter=letter)


if __name__ == "__main__":
    app.run(debug=True)
