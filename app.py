import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Hello World!\n--Team 3'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2503))
    app.run(debug=True,host='0.0.0.0',port=port)
