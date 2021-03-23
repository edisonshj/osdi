from flask import Flask
from flask import render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('TTT.html')

@app.route('/aaa',methods=['GET'])
def aaa():#名子可隨便取
    account = request.args["fname"]
    password = request.args["lname"]
    namelist = {'user1':'password1'}
    if(account in namelist and password == namelist[account]):
        return '登入成功'
    else: return '登入失敗'
    data =request.args
    return data

@app.route('/loginaaa')
def login():
    return 'loginYYYYYTTTTTT'
    
if __name__ == '__main__':
    app.debug = True
    app.run()