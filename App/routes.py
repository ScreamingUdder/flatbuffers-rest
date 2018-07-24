from App import app
from flask import render_template,flash, redirect
from App.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template("standard.html",title = 'Page 1')

@app.route('/form', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.Field1.data, form.CheckBox.data))
        return redirect('/index')
    return  render_template("form.html",title = 'Form',form = LoginForm())