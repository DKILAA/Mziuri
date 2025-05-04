from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            c = float(request.form["c"])
            operator = request.form["operator"]

            if operator == "+":
                result = a + b + c
            elif operator == "*":
                result = a * b * c
            else:
                result = "Invalid operator"
        except ValueError:
            result = "Please enter valid numbers"
    
    return render_template("index.html", result=result)
