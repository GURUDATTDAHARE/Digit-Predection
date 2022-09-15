import pickle
from flask import Flask, render_template, request, jsonify, make_response
import numpy as np
import PIL.Image as Image
import io
import base64
import cv2
import tensorflow as tf
from werkzeug.utils import redirect
import ast

app = Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/predict', methods=["POST"])
def predict():
    modal = tf.keras.models.load_model('my_model.h5')
    dict = ast.literal_eval(request.data.decode('utf-8')) # to convert byte to dict
    s = dict["imageURL"]
    url = s[22:]
    encoded_string = url.encode()
    byte_array = bytearray(encoded_string)
    b = base64.b64decode(byte_array)
    img = Image.open(io.BytesIO(b))
    img = np.array(img)
    img = img[:, :, ::-1].copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resied = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    newimg = tf.keras.utils.normalize(resied, axis=1)
    newimg = np.array(newimg).reshape(-1, 28, 28, 1)
    predict = modal.predict(newimg)
    ans = np.argmax(predict)
    return make_response(jsonify({"img": ans.item()}))


if __name__ == "__main__":
    app.run(debug=True)
