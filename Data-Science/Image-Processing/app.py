from process_image import ProcessImage
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv
load_dotenv()

image = ProcessImage()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap5(app)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("filename")
        if not file or file.filename == "":
            return render_template("index.html", error="No file selected")
        top_colors = image.process_image(file)
        return render_template("index.html", colors=top_colors)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)