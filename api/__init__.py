# Flask — this is the web framework that we use
from flask import Flask

# Flask-Cors — an extension for Cross Origin Resource Sharing
from flask_cors import CORS

# Flask-SQLAlchemy — an ORM that makes it easier for us to communicate with our SQL database
from flask_sqlalchemy import SQLAlchemy


# Instantiating Flask App
app = Flask(__name__)
# Cross Origin Resource Sharing
CORS(app)

# Handling heroku error
uri = "postgres://sdbeisoj:r2otWxre-Q6Vj1CIsyO2auK53u38q92c@castor.db.elephantsql.com/sdbeisoj"
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# Flask App configuration for DB
app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Instantiating DB
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Employee API!!'
