from App import app
from flask import render_template, flash, redirect, request, jsonify, abort
from App.kafka_helpers import poll_messages
from App.form import LoginForm
from App.errors import error


@app.route('/')
@app.route('/index')
def index():
    return render_template("standard.html", title='Page 1')


@app.route('/form', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.Field1.data, form.CheckBox.data))
        return redirect('/index')
    return render_template("form.html", title='Form', form=LoginForm())


@app.route('/requests', methods=['GET', 'POST'])
def requests():
    if request.method == 'GET':
        try:
            output = poll_messages(request.args.get('topic'), request.args.get('broker'), request.args.get('numofmessages'))
        except Exception as e:
            return error(400, str(e))

        return jsonify(output)
    else:
        return error(405, 'Invalid HTTP request')

    #     if not requests:
    #         abort(400)
    #         return redirect('/')
    #     elif not requests['topic']:
    #         abort(400)
    #         return redirect('/')
    #     elif not requests['num_of_messages']:
    #         abort(400)
    #         return redirect('/')
    #     elif not requests['broker']:
    #         abort(400)
    #         return redirect('/')
    #     else:
    #         return jsonify(requests)
    # else:
    #     abort(400)
    #     return redirect('/')
