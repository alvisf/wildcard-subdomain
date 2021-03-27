from flask import Flask,redirect,request
from alvisapp import alvis

app = Flask(__name__)
app.config['SERVER_NAME'] = 'tactii.com'

@app.route('/', subdomain="<tenant>")
def index(tenant):
    if tenant=="alvis":
        return alvis()
        #rest=requests.get('http://54.203.114.23:8081')

        #return rest
    return "Tenant Name:" + tenant

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)