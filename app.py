import os
from flask import Flask, render_template, request, url_for,redirect
from dog_try import faceSwap
import cv2,base64
from urllib.parse import quote

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'


@app.route('/results', methods=["GET", "POST"])
def results():
    if request.method == "POST":
        image1 = request.files['image1']
        image2 = request.files['image2']
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], image1.filename)
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], image2.filename)

        image1.save(path1)
        image2.save(path2)
        
        result_from_landmarks = faceSwap(path1, path2)
        im1 = cv2.imread(path1)
        im2 = cv2.imread(path2)

        retval, buffer1 = cv2.imencode('.jpg', im1)
        im1txt = f'data:image/png;base64,{quote(base64.b64encode(buffer1))}'

        retval, buffer2 = cv2.imencode('.jpg', im2)
        im2txt = f'data:image/png;base64,{quote(base64.b64encode(buffer2))}'



        os.remove(path1)
        os.remove(path2)
        return render_template("results.php", result=result_from_landmarks,image1=im1txt,image2=im2txt)
    else:
        return render_template("results.php", result={})
    


@app.route('/')
def index():
    if request.method == "GET":
        return render_template("index.php")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)