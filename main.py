from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConVo Servers</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url('https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/d747babd631fa52cdee048111b1ccb77.jpg');
            background-size: cover;
            background-position: center;
            font-family: Arial, sans-serif;
            color: white;
        }
        .header {
            text-align: center;
            padding: 50px;
            font-size: 36px;
            font-weight: bold;
            color: #ffffff;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }
        .box {
            width: 300px;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            text-align: center;
        }
        .box img {
            width: 100%;
            border-radius: 10px;
            cursor: pointer; /* To indicate it's clickable */
        }
        .convo-button {
            margin-top: 50px;
            padding: 10px 20px;
            font-size: 18px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .convo-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="header">FeeL PowEr Of Faizu <3</div>
    <button class="convo-button" onclick="showConvoPage()">Go to ConVo Servers</button>

    <div class="container" id="convo-page" style="display:none;">
        <div class="box">
            <h3>CONVO 1</h3>
            <a href="https://apk-c2xf.onrender.com/" target="_blank">
                <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/db317a92acb66c6552b79e27d3c3da3b.jpg" alt="Convo 1">
            </a>
        </div>
        <div class="box">
            <h3>CONVO 2</h3>
            <a href="https://apk-2.onrender.com/" target="_blank">
                <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/ac9df70b335a014d67530a81991a5df5.jpg" alt="Convo 2">
            </a>
        </div>
        <div class="box">
            <h3>CONVO 3</h3>
            <a href="https://apk-1-qwk3.onrender.com/" target="_blank">
                <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/0cf19c8b44e24cace8d691bc7f0b2198.jpg" alt="Convo 3">
            </a>
        </div>
        <div class="box">
            <h3>CONVO 4</h3>
            <a href="https://apk-3.onrender.com/" target="_blank">
                <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/a302a5e258af91dbe497739c1457923e.jpg" alt="Convo 4">
            </a>
        </div>
        <div class="box">
            <h3>CONVO 5</h3>
            <a href="https://the-faizu-brand.onrender.com/" target="_blank">
                <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/a23fab98a18b12536ed9cb5c64da831a.jpg" alt="Convo 5">
            </a>
        </div>
    </div>

    <script>
        function showConvoPage() {
            document.getElementById('convo-page').style.display = 'block'; // Show ConVo page when button is clicked
        }
    </script>

</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
