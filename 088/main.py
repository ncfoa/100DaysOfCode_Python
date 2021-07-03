import json

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class TodoForm(FlaskForm):
    todo = StringField('todo', validators=[DataRequired()])
    date = DateField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_todo():
    form = TodoForm()
    if form.validate_on_submit():
        with open("todos.json", mode="r") as fr:
            data = json.loads(fr.read())
        with open("todos.json", "w") as fw:
            entry = {"todo": form.todo.data, "due date": str(form.date.data)}
            data.append(entry)
            fw.write(json.dumps(data))
        return redirect(url_for('todos'))
    return render_template('add.html', form=form)


@app.route('/todos')
def todos():
    with open('todos.json', 'r') as r:
        data = json.loads(r.read())
        r.close()
    return render_template('todos.html', todos=data)


if __name__ == '__main__':
    app.run(debug=True)
