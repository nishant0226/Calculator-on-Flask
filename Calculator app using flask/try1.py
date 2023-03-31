import math
from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template("index.html")
@app.route("/math",methods=["POST"])
def math_ops():
    if request.method=='POST':
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if ops=='add':
            r=num1+num2
            result="the add of"+str(num1)+"and"+str(num2)+"is"+str(r)
        if ops=='subtract':
            r=num1-num2
            result="the sub of"+str(num1)+"and"+str(num2)+"is"+str(r)
        if ops=='divide':
            r=num1/num2
            result="the divide of"+str(num1)+"and"+str(num2)+"is"+str(r)
        if ops=='multiply':
            r=num1*num2
            result="the multiply of"+str(num1)+"and"+str(num2)+"is"+str(r)
        if ops=='log':
            r=math.log(num1,num2)
            result="the add of"+str(num1)+"and"+str(num2)+"is"+str(r)
        return render_template("results.html",result=result) 


if __name__=="__main__":
    app.run(host="0.0.0.0")