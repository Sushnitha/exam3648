from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/greet',methods=['POST'])
def greet():
    name=request.form['name']
    age=request.form['age']
    return render_template('greetings.html',name=name,age=age)
if __name__==("__main__"):
    app.run(host="0.0.0.0",debug=True)
