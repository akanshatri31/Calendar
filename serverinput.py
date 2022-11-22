from flask import Flask
appname = Flask(__name__)
@appname.route('/hello/<name>')
def input_server(name):
    return 'Hello %s!' % name
if __name__ == '__main__':
    appname.run(host='0.0.0.0',port=50100, debug=False)
