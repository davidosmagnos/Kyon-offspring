<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KYON: Offspring Generator</title>
    <link rel="stylesheet" href="../static/style-result.css">
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
    

    <div class="body-bg-yellow">
    <div class="topRect">
        <div class="appName">
            <h1 id="txt-ky-title">Kyon</h1>
            <p id="txt-ky-desc">Scan, Classify, and Generate</p><br>
            
        </div>
    </div>
    

    
    <form form method="post" enctype="multipart/form-data">
        <div class="row" id="formOutput">
            <div class="column">
                <img src="../static/dog1.jpg" alt="" id="img1" class="img-left">
            </div>
            <div class="column">
                <h1 style="color:white;">+</h1>
            </div>
            <div class="column">
                <img src="../static/placeholder_img.png" alt="" id="img2" class="img-right">
            </div>
        </div>
        
        
        <div class="generate">
            <div class="circle-pic">
                <!-- <img src="../static/dog1.jpg" alt="face with landmarks" class="result"> for ui designining purposes-->
                {% if result and result.error %}
                    <p>{{ result.error }}</p>
                {% elif result and result.image_with_landmarks %}
                    <p><img src="{{ result.image_with_landmarks }}" alt="face with landmarks" class="result"></p>
                {% endif %}
            </div>
            <div class="bottom-img">
                <img src="../static/login_banner.png" class="overlapped-img">
            </div>
            
        </div>
    </form>

    <div class="bg">
        
        <div class="circle"></div>
    </div>
    
</div>

</body>
</html>