from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return jsonify({'sent': request.get_json()}, 201)
    return jsonify({'about':"Hello World!"})


@app.route("/divide/<int:num1>/<int:num2>", methods=['GET'])
def get_divide(num1, num2):
    return jsonify({'result':num1/num2})

if __name__ == '__main__':
    app.run(debug=True)
