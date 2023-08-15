from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def render_server():
    return render_template('n-queens.html')


@app.route('/', methods=['POST'])
def N_queens():
    if request.method == 'POST':
        n_queens_input = request.args.get('n_queens_input', type=int)
        return jsonify({"state_code": 200, "n_queens_input": n_queens_input, "result": "Your result here"})


if __name__ == "__main__":
    app.run(debug=True, port=3008)