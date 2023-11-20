from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder="templates")

todos = [{'task':"Sample todo", "done": False}]

""" '@' decorator function in Python
use: defines a route in a Flask application, and when a user accesses the root URL, 
it calls the index function, which renders an HTML template and passes a variable (todos) 
to that template, which can be used to display dynamic data in the web page"""
@app.route('/')
def index():
    return render_template("index.html", todos = todos)

@app.route('/add',methods = ['POST'])
def add():
    todo = request.form['todo']
    todos.append({'task':todo,'done':False})
    return redirect(url_for("index"))

@app.route('/edit/<int:index>', methods = ['GET','POST'])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form['todo']
        return redirect(url_for('index'))
    else:
        return render_template('edit.html',todo = todo, index = index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('index'))



# Code is executed only when file is excuted as main file.
if __name__ == "__main__":
    app.run(debug=True)