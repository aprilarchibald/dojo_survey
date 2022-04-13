from flask import Flask, render_template, redirect, request, session
app=Flask(__name__)
app.secret_key ='security'


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    print(request.form)
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comments']= request.form['comments']
    return redirect('/result')

@app.route('/result')
def show_form_data():
    return render_template('show.html')

@app.route
def clear():
    session.clear()
    return redirect('/')


if __name__=="__main__":
	app.run(debug=True)
