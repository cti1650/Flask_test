# -*- coding: utf-8 -*-

import os
from flask import Flask

@app.route("/")
def index():
    return {"Hello": "World"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, debug=True)
