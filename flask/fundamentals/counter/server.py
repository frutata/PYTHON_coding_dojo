from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "secret tunnel"

#=============================
# Default Route
#=============================

@app.route('/')
def index():

    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0

    return render_template("index.html", count = session["count"])

#=============================
# Add +2 Count Route
#=============================

@app.route('/add')
def add():
    session["count"] += 1

    return redirect("/")

#=============================
# Reset Session
#=============================

@app.route("/destroy_session")
def reset_session():
    session.clear()
    return redirect("/")

















if __name__=="__main__":
    app.run(debug=True)