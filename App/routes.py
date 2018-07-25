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
            flash('Requesting data from the {} topic in the {} broker, requesting {} messages'.format(
                form.Field2.data, form.Field1.data, form.IntField.data))
            return redirect('/requestmidpoint')
        elif form.check_high_low.data:
            flash('Checking the high and low offsets of the {} topic in the {} broker'.format(
                form.Field2.data, form.Field1.data))
            return redirect('/requestmidpoint')
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
