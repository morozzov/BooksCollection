from flask import Flask, render_template, request, redirect, jsonify
from models.user import User
from models.book import Book
from db.DB import DB
import json

app = Flask(__name__)
db = DB()

@app.route('/', methods = ['POST', 'GET'])
def signin():
    if  request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        access = db.GetUser(login, password)

        if access == True:
            return redirect('/main')

    else:
        return render_template('signin.html')

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if  request.method == "POST":
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']

        user = User(name,login,password)

        db.WriteUser(user)
        return redirect('/')

    else:
        return render_template('signup.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/main')
def mainh():
    data = db.GetAllEmployees()
    return render_template('main.html', data = data, len = len(data['Books']))


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtauthor = request.form['txtauthor']
        txtyear = request.form['txtyear']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'
        elif txtauthor == '':
            msg = 'Please Input Department'
        elif txtyear == '':
            msg = 'Please Input Phone'
        else:
            db.WriteBook(Book(txtname, txtauthor, txtyear))
            msg = 'New record created successfully'
    return jsonify(msg)




if __name__ == '__main__':
    app.run()