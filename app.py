#!flask/bin/python
import dropbox
from auth import *
from flask import Flask, jsonify, abort, make_response, request

TOKEN = "????????????????????????"

app = Flask(__name__)
dbx = dropbox.Dropbox(TOKEN)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/dbx-store/api/v1.0/files/', methods=['GET'])
def get_files():
    files = []
    for entry in dbx.files_list_folder('').entries:
        md, res = dbx.files_download('/' + entry.name)
        data = str(res.content)
        files.append({'data': data, 'name': entry.name})
    return jsonify({'files': files})


@app.route('/dbx-store/api/v1.0/files/<name>', methods=['GET'])
def get_file(name):
    try:
        md, res = dbx.files_download('/' + name)
    except dropbox.exceptions.ApiError:  # such file doesn't exist
        abort(404)
    data = str(res.content)
    return jsonify({name: data})


@app.route('/dbx-store/api/v1.0/files/<name>', methods=['PUT'])
@auth.login_required
def update_file(name):
    file = request.json
    if not file:
        abort(400)
    file['name'] = name
    try:
        dbx.files_delete_v2('/' + file['name'])
    except dropbox.exceptions.ApiError:
        pass
    dbx.files_upload(bytes(file['data'], 'utf-8'),
                     '/' + file['name'])

    return jsonify(file)


if __name__ == '__main__':
    app.run(debug=True)
