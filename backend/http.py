from app import app

from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login'
    else:
        return 'showform'
    
app.get('/login')
def login_get():
    return "login"

@app.post('/login')
def login_post():
    return "do it"