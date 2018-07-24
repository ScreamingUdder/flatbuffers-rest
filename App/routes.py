from App import app
from flask import render_template,flash, redirect, request, jsonify, abort
from App.kafka_helpers import topic_exists,broker_exists
from App.form import LoginForm
from App.errors import error

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


@app.route('/requests',methods=['GET','POST'])
def requests():
    if request.method == 'GET':
        requests = {}
        requests['broker'] = request.args.get('broker')
        if not broker_exists(requests['broker']):
            return error(400,'Broker missing')

        requests['topic'] = request.args.get('topic')
        if not topic_exists(requests['topic'],requests['broker']):
            return error(400,'Topic missing')
        try:
            requests['numofmesssages'] = int(request.args.get('numofmessages'))
        except ValueError as e:
            return(error(400,str(e)))


        return jsonify(requests)
    else:
        return error(405,'Invalid HTTP request')






    #
    #     if not requests:
    #         abort(400)
    #         return redirect('/')
    #     elif not requests['topic']:
    #         abort(400)
    #         return redirect('/')
    #     elif not requests['numofmesssages']:
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

















