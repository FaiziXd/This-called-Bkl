from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # HTML content with embedded CSS and JS
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>New Choice Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f4;
            }
            img {
                width: 80%;
                max-width: 600px;
                margin-top: 50px;
            }
            .options {
                margin-top: 20px;
            }
            .option {
                display: inline-block;
                margin: 10px 20px;
                padding: 10px 20px;
                background-color: #ff5733;
                color: white;
                font-size: 20px;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .option:hover {
                background-color: #c0392b;
            }
            #message {
                margin-top: 20px;
                font-size: 24px;
                color: #ff5733;
            }
        </style>
    </head>
    <body>
        <img src="https://raw.githubusercontent.com/FaiziXd/Lun-dhek-le-aja/refs/heads/main/b3a11a76885e51f067433c05a1d8fb3d.jpg" alt="Convo Image">
        
        <div class="options">
            <div class="option" onclick="showPostMessage()">POST</div>
            <div class="option" onclick="window.location.href='https://faizu-tn8o.onrender.com'">CONVO</div>
            <div class="option" onclick="window.location.href='https://youtube.com/@faiizuxd?si=Nn1ZpnT7IThp4lRl'">YOUTUBE</div>
        </div>

        <div id="message"></div>

        <script>
            function showPostMessage() {
                document.getElementById('message').innerHTML = 'Wait! Post server is coming Soon >3';
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
