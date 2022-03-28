import os

from flask import (Flask, render_template, redirect, request,
                   make_response, url_for, session, abort,
                   send_from_directory, send_file)

app = Flask(__name__)

d = {}
print(d)


@app.route('/', methods=['POST', 'GET'])
def home():
    print(request.method)
    if request.method == "POST":
        print(request.method)
        Name = request.form['Name']
        Age = request.form['Age']
        Phonenumber = request.form['Phonenumber']
        print(f"{Name},{Age},{Phonenumber}")

        d["Name"] = Name
        d["Age"] = Age
        d["Phonenumber"] = Phonenumber
        print(d)
        return render_template("result.html", result=d)
    else:
        return render_template("practice.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
