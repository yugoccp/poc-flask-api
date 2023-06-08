from http.client import HTTPException
from flask import Flask, json
import api.storage_sample_api as storage_api
import api.crud_sample_api as crud_api

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World!"

@app.errorhandler(HTTPException)
def handle_exception(e):
	response = e.get_response()
	response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
	})
	response.content_type = "application/json"
	return response

app.add_url_rule('/storage/upload/<filename>', view_func=storage_api.upload)
app.add_url_rule('/storage/download/<filename>', view_func=storage_api.download)
app.add_url_rule('/crud/create/<name>', view_func=crud_api.create)
app.add_url_rule('/crud/update/<name>', view_func=crud_api.update)
app.add_url_rule('/crud/delete/<name>', view_func=crud_api.delete)
app.add_url_rule('/crud/list', view_func=crud_api.list)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)