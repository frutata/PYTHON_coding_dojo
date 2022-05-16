from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "secret tunnel"

# ============================================
# Form Routes
# ============================================

@app.route('/')
def index():

    if 'user' in session:
        print('user exists!')
    else:
        print("key 'user' does NOT exist")

    if "count" in session:
        #do something, count+1
        session["count"] += 1
    else:
        session["count"] = 0

    return render_template("index.html", count = session["count"])

@app.route('/users', methods=["POST"])
def process_user():
    print(request.form)
    print(request.form["username"])
    print(request.form["email"])
    print("this is the processing route")
    username = request.form["username"]

    print(f"{username} was here!")
    #print form info

    session["user"] = request.form["username"]

    return redirect("/show")

# ============================================
# Show Form Info Route
# ============================================

@app.route("/show")
def show_user_info():
    print("========" + session["user"])
    return render_template("show.html", user_name = session["user"])

# ============================================
# Reset Session to Empty
# ============================================

@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")











if __name__=="__main__":
    app.run(debug=True)