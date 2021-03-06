# -*- coding: utf-8 -*-

import os
from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route("/")
def index():
    return {"text": "Hello World!!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)
