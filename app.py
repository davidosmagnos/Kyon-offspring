import os
from flask import Flask, render_template, request, url_for,redirect
from dog_try import faceSwap
import dog_try
import cv2,base64
from urllib.parse import quote
import sqlite3
import datetime

conn = sqlite3.connect("kyonDB.db")




def getFname(fname:str):
    name,type = fname.split(".")
    return name

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'pics'


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

        imName = getFname(image1.filename)
        imName2 = getFname(image2.filename)
        resName = f"{imName+imName2}.jpg"

        cv2.imwrite(f"pics/results/{resName}",result_from_landmarks["image"])

        conn = sqlite3.connect("kyonDB.db")
        conn.execute("CREATE TABLE IF NOT EXISTS uploads(upId INTEGER PRIMARY KEY,img1 TEXT,img2 TEXT,result TEXT,logDate TEXT);")
        conn.execute(f"INSERT INTO uploads(img1,img2,result,logDate)VALUES('{image1.filename}','{image2.filename}','{resName}','{str(datetime.datetime.now())}')")
        conn.commit()
        conn.close()
        
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