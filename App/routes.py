from App import app
from flask import render_template, flash, redirect, request, jsonify
from App.kafka_helpers import poll_messages, check_offsets
from App.form import RequestForm
from App.errors import error


@app.route('/form', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def request_form():

    form = RequestForm()
    if form.validate_on_submit():
        if form.check_messages.data:
            try:
                output = poll_messages(form.Field2.data, form.Field1.data, str(form.IntField.data))
            except Exception as e:
                return error(400, str(e))
            return jsonify(output)
        elif form.check_high_low.data:
            try:
                output = check_offsets(form.Field2.data,form.Field1.data)
            except Exception as e:
                return error(400, str(e))
            return jsonify(output)
    return render_template("form.html", title='Form', form=RequestForm())


@app.route('/requestmidpoint')
def request_form_data():
    return render_template("form_submitted.html", title="Form Submitted")


@app.route('/requests', methods=['GET', 'POST'])
def requests():
    if request.method == 'GET':
        if request.args.get('offsets'):
            try:
                output = check_offsets(request.args.get('topic'), request.args.get('broker'))
            except Exception as e:
                return error(400, str(e))
        else:
            try:
                output = poll_messages(request.args.get('topic'),
                                       request.args.get('broker'),
                                       request.args.get('numofmessages'))
            except Exception as e:
                return error(400, str(e))

        return jsonify(output)
    else:
        return error(405, 'Invalid HTTP request')
