from flask import Flask, render_template, request, Flask
import sqlite3
import os

currentdirectory = (postgres://uhrljkvagsdvbp:2b4c30d656d914d2da0a7fd00f814ff90f4b929f5e118341415ed194d56d8841@ec2-34-193-112-164.compute-1.amazonaws.com:5432/dcl1cish3o860t)

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("ex.html")


@app.route("/logincode", methods=["POST"])
def phonebook():
    name = request.form["textfield"]
    phonenumber = request.form["textfield1"]
    connection = sqlite3.connect(currentdirectory + "\phoneBook.db")
    cursor = connection.cursor()
    query1 = "INSERT INTO phone VALUES('{n}','{pnm}')".format(n=name, pnm=phonenumber)
    cursor.execute(query1)
    connection.commit()
    return '''<script>alert("SUCCESS");window.location='/'</script>'''

@app.route("/resultpage", methods=["GET"])
def resultpage():
    try:
        if request.method == "GET":
            name = request.args.get("NAME")
            connection = sqlite3.connect(currentdirectory + "\phonebook.db")
            cursor = connection.cursor()
            query = "SELECT  * from phone"
            result = cursor.execute(query)
            result = result.fetchall()
            return render_template("Resultpage.html", values=result)
    except:
        return render_template("resultpage.html", values="")

if __name__ == '__main__':
    app.run(debug=True)
