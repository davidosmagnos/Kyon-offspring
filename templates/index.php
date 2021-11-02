<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KYON: Offspring Generator</title>
    <link rel="stylesheet" href="../static/style.css">
</head>
<!-- <body>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="image1" placeholder="Upload an dog image 1"><br>
        <input type="file" name="image2" placeholder="Upload an dog image">
        <button>Send</button>
    </form>
    <div style="background: #f6f6f6; padding: 20px; margin-top: 20px;">
        <strong>Result with landmarks</strong>
        {% if result and result.error %}
            <p>{{ result.error }}</p>
        {% elif result and result.image_with_landmarks %}
            <p><img src="{{ result.image_with_landmarks }}" alt="face with landmarks"/></p>
        {% else  %}
            <p>The results will be placed here</p>
        {% endif %}
    </div> -->

    <div class="topRect">
        
    </div>
    <div class="appName">
        <h1>Kyon</h1>
        <p>Scan, Classify, and Generate</p><br>
        <h4>Offspring Generator</h4>
    </div>
    <form method="post" enctype="multipart/form-data" action="http://192.168.68.105:5000/results">
        <div class="formButtons">
            <label for="image1">
                <input type="file" name="image1" id="image1" hidden onchange="loadFile('img1')">
               <img src="../static/placeholder_img.png" alt="" id="img1">
            </label>
            <h1 style="color:white;">+</h1>
            <label for="image2">
                <input type="file" name="image2" id="image2" hidden onchange="loadFile('img2')">
               <img src="../static/placeholder_img.png" alt="" id="img2">
            </label>
        </div>
        <div class="generate">
            <button>
                <p>Generate<br>Offspring</p>
                <!-- {% if result and result.error %}
                    <p>{{ result.error }}</p>
                {% elif result and result.image_with_landmarks %}
                    <p><img src="{{ result.image_with_landmarks }}" alt="face with landmarks" class="result"></p>
                {% endif %} -->
            </button>
        </div>
    </form>

    <div class="bg">
        
        <div class="circle">
            <img src="../static/guess.png" class="img-guess">
        </div>
    </div>
    


</body>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>
    $('document').ready(function () {
    $("#image1").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#img1').attr('src', e.target.result);
            }
            reader.readAsDataURL(this.files[0]);
        }
    });
});

$('document').ready(function () {
    $("#image2").change(function () {
        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#img2').attr('src', e.target.result);
            }
            reader.readAsDataURL(this.files[0]);
        }
    });
});
</script>
</html>