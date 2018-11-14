from flask import Flask, render_template
from data import Employee

app=Flask(__name__)
getEmployee=Employee()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/employee')
def employee():
    return render_template('employee.html',myEmployee=getEmployee)

if(__name__=='__main__'):
    app.run(debug=True)
