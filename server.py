from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)    
app.secret_key = 'ExyWzo;Ffpza,gr'



@app.route('/')
def home():
    if 'x' in session:
        print('count exists!')
    else:
        print("count does NOT exist")
    if 'x' in session:
        session['x'] +=1
    else:
        session['x']=0
    return render_template('index.html', x = session['x'])

@app.route('/2')
def two():
    if 'x' in session:
        session['x'] += 2
    return render_template('index.html', x = session['x'])


@app.route('/destroy_session')
def reset():
    session.clear()	# clears all keys
    return redirect ('/')





if __name__=="__main__":   
    app.run(debug=True)  