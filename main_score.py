from flask import Flask
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/score')
def score_server():
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            score = file.read().strip()
        return f"""
        <html>
            <head>
            <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is:</h1>
                <div id="score">{score}</div>
            </body>
        </html>    
    """
    except Exception as e:
        return f"""
            <html>
                <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR:</h1>
                <div id="score" style="color: red;">{e}</div>
            </body>
        </html>
    """, BAD_RETURN_CODE

# if __name__ == '__main__':
#   app.run(port=5000)
