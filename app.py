import os
from flask import Flask, render_template, request, url_for, redirect
from dog_try import faceSwap

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'


@app.route('/results/<file1>/<file2>/')
def results(file1, file2):
    path1 = file1
    path2 = file2
    result_from_landmarks = faceSwap(path1, path2)
    os.remove(path1)
    os.remove(path2)
 
    return render_template("results.php", result=result_from_landmarks)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.php", file1 ={}, file={})
    else:
        image1 = request.files["image1"]
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], image1.filename)
        image1.save(path1)

        image2 = request.files["image2"]
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], image2.filename)
        image2.save(path2)

        
        return redirect(url_for('results',file1 = path1, file2= path2))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)