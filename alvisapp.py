from flask import Flask
app = Flask(__name__)

@app.route('/')
def alvis():
    return "This is alvis app"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)