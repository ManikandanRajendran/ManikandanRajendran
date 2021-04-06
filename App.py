import os
from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")


def write_to_text(data):
    with open('database.txt', 'a') as db:
        print(db)
        email = data['email']
        sub = data['subject']
        msg = data['message']
        db.write(f'\n{email},{sub},{msg}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as db1:
        email = data['email']
        sub = data['subject']
        msg = data['message']
        csv_writer = csv.writer(db1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, sub, msg])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('/thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
