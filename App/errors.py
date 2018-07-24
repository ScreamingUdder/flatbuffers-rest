from flask import jsonify

def error(code,message):

    return jsonify(status=code,message=message)


