from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>Hello World!</h1>
    <h2>I'm living inside a Docker container, Yay!</h2>
    <h3>Sooo, I'm actually quite cool :)</h3>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)