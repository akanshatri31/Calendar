from flask import Flask
app = Flask(__name__)

@app.route('/date/<int:date>')
def hello_name(date):
    if date <= 231122:
        return{'Valid': date}
    else:
        return 'Invalid date'

if __name__ == '__main__':
   app.run(host= '0.0.0.0', port = 5000, debug = True)