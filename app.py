import pickle
from flask import Flask, render_template, request
import numpy as np
import PIL.Image as Image
import io
import base64
import cv2
import tensorflow as tf
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def helloWorld():
    if request.method == "GET":
        return render_template('home.html')
    else:
       # print(request.get_data)
        return redirect("/predict")


@app.route('/predict', methods=["POST", "GET"])
def predict():
    modal = tf.keras.models.load_model('my_model.h5')
    s = request.form["CityName"]
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
    # print(type(ans))
    if ans == 1:
        return render_template('1_res.html')
    elif ans == 2:
        return render_template('2_res.html')
    elif ans == 3:
        return render_template('3_res.html')
    elif ans == 4:
        return render_template('4_res.html')
    elif ans == 5:
        return render_template('5_res.html')
    elif ans == 6:
        return render_template('6_res.html')
    elif ans == 7:
        return render_template('7_res.html')
    elif ans == 8:
        return render_template('8_res.html')
    elif ans == 9:
        return render_template('9_res.html')
    else:
        return render_template('0_res.html')


if __name__ == "__main__":
    app.run(debug=True)
