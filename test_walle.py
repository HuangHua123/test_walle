from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

@app.route('/getUser/', methods=['GET'])
def getUser():
	name = "张三"
	sex = "男"
	age = "24"
	results = {
		"名字":name,
		"性别":sex,
		"年龄":age
	}
	response = make_response(jsonify(results))
	response.headers['Content-Type'] = 'application/json;charset=UTF-8'
	response.headers['Server'] = ''
	return response
 
if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=5014, debug=False, use_reloader=False)