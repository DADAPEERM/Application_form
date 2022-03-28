import os
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import FileStorage
from flask import (Flask, render_template, redirect, url_for,
                   request, make_response, session, abort,
                   send_file, send_from_directory)
# from werkzeug import secure_filename
app = Flask(__name__)
#app.secret_key = 'secret'
#app.config["IMAGE_UPLOADS"] = "D:/flask/images"

#app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

d = {}
print(d)


@app.route('/', methods=['POST', 'GET'])
def home():
    print(request.method)
    if request.method == "POST":
        print(request.method)
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        print(f"{name},{age},{phone}")

        d["name"] = name
        d["age"] = age
        d["phone"] = phone
        print(d)
        return render_template("result.html", result=d)
    else:
        return render_template("home1.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
