from flask_app import app

from flask_app.controllers import user_con
from flask_app.controllers import guide_con


if __name__=="__main__":
    app.run(debug=True)