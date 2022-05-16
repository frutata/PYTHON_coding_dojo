from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def check1():
    return render_template("index.html", num = 8)

@app.route('/<int:num>')
def check2(num):
    return render_template("index.html", num = num)

if __name__=="__main__":
    app.run(debug=True)