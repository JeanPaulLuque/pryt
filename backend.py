from flask import Flask ,render_template,url_for, redirect, jsonify,session, request, g
import time

add=Flask(__name__)
add.secret_key='dwqqqqqqqqqqqqqqqqqqqqqqqqdqwkdoqwkodwqodwkoko'

user=["admin"]
pasw=["admin"]

@add.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session.pop('user_id', None)

        name=request.form['nameuser']
        paw=request.form['pass']
        for i in range(len(user)):
            if paw == pasw[i] and name== user[i]:
                session['user']=name
                return redirect(url_for('app'))

    return render_template('index.html')

@add.route('/register')
def regis():
    return render_template('register.html')

@add.route('/regis',methods=['POST'])
def add_count():
    if request.method == 'POST':
        name=request.form['nameuser']
        paw=request.form['pass']
        user.append(name)
        pasw.append(paw)
        return redirect(url_for('index'))
    return redirect(url_for('register'))

@add.route('/app')
def app():
    if g.user:
        return render_template('app.html',user=session['user'])
    return redirect(url_for('index'))

@add.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']

@add.route('/drop')
def drop():
    session.pop('user',None)
    return render_template('index.html')

if __name__=="__main__":
    add.run(port=3000,debug=True)
