<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KYON: Offspring Generator</title>
    <style>
            
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;600;900&display=swap');

*{
    margin: 0;
    padding: 0;
}
body {
	background-color:#0f0f0f;
    overflow: hidden;
}

.topRect{
    width: 16em;
    height: 2.3em;
    background-color: #CDD1DE;
    margin-left: auto;
    margin-right: -9px;
    margin-top: -15px;
    border-radius: 25px;
}

.appName{
    color:#eda61c;
    font-family: 'Montserrat-Black', sans-serif;
    
    margin-left: 1em;
}
.appName h1{
    font-family: 'Montserrat';
    margin: 3px;
}

.appName h1,.appName p,.appName h4{
    margin: 3px;
}

.appName h4{
    color: white !important;
    text-align: center;
}

.formButtons{
    background-color: #f4d482;
    width: 95%;
    height:10em;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
    margin-top: 1em;
}
.formButtons img{
    width: 100px;
    height: 100px;
    background-color: #CDD1DE;
    border:2px solid #4da1a9;
    border-radius: 20px;
    margin-top: 30px;
    margin-left: 2em;
}


.formButtons h1{
    display: inline;
    position: relative;
    bottom:1.5em;
    left:.6em;
}

.generate{
    margin-top: 3em;
    width:fit-content;
    margin-left: auto;
    margin-right: auto;
    
}

.generate button{
    width: 15em;
    height: 15em;
    background-color: #4da1a9;
    border-radius: 100%;
    border-style: none;
    color: white;
    font-weight: bold;
}

.generate:hover button{
    width: 15em;
    height: 15em;
    background-color: #448d94;
    border-radius: 100%;
    border-style: none;
    color: white;
    font-weight: bold;
}

.generate .result{
    width: 15em;
    height: 15em;
    background-color: transparent;
    border-radius: 100%;
    border-style: none;
}
.circle{
    background-color: #CDD1DE;
    width: 30em;
    height: 30em;
    border-radius: 100%;
    margin-left: -3.7em;
    margin-top: -6em;
    align-items: center;
}



    </style>
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
    <div class="appName">
        <h1>Kyon</h1>
        <p>Scan, Classify, and Generate</p><br>
        <h4>Offspring Generator</h4>
    </div>
        
    </div>
    
    <form form method="get" enctype="multipart/form-data">
        <div class="formButtons">
            <label for="image1">
                <input type="file" name="image1" id="image1" hidden onchange="loadFile('img1')">
                {% if result and result.error %}
                    <p>{{ result.error }}</p>
                {% elif result and result.image_with_landmarks %}
                    <p><img src="{{ result.image_with_landmarks }}" alt="face with landmarks" class="result"></p>
                {% endif %}
            </button>
            </label>
            <h1 style="color:white;">+</h1>
            <label for="image2">
                <input type="file" name="image2" id="image2" hidden onchange="loadFile('img2')">
               <img src="../static/placeholder_img.png" alt="" id="img2">
            </label>
        </div>
        <div class="generate">
           
                {% if result and result.error %}
                    <p>{{ result.error }}</p>
                {% elif result and result.image_with_landmarks %}
                    <p><img src="{{ result.image_with_landmarks }}" alt="face with landmarks" class="result"></p>
                {% endif %}
            
        </div>
    </form>

    <div class="bg">
        
        <div class="circle"></div>
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