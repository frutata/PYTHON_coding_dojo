from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "secret tunnel"

#=============================
# Default Route
#=============================

@app.route('/')
def index():

    return render_template("index.html")

#=============================
# Form Process Route
#=============================

@app.route('/process', methods=["POST"])
def process():

    print(request.form)
    print(request.form["username"])
    print(request.form["location"])
    print(request.form["language"])
    print(request.form["comment"])
    username = request.form["username"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    print(f"{username} lives in {location} and speaks {language}! Fun fact about them: '{comment}'!")
    
    session["student"] = request.form["username"]
    session["place"] = request.form["location"]
    session["speak"] = request.form["language"]
    session["other"] = request.form["comment"]

    return redirect("/result")

#=============================
# Form Result Route
#=============================

@app.route("/result")
def result():

    print(session["student"])
    print(session["place"])
    print(session["speak"])
    print(session["other"])

    return render_template("result.html", user_name = session["student"], dojo_location = session["place"], fav_language = session["speak"], other_comment = session["other"])

















if __name__=="__main__":
    app.run(debug=True)