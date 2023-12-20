from flask_sqlalchemy import SQLAlchemy
import json
db = SQLAlchemy()

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(12), nullable=False, unique=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    last_login = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(10), nullable=False, default='unactive')
    roles = db.relationship('Role', backref='user', uselist=False)


class Role(db.Model):
    rid = db.Column(db.Integer, primary_key=True, nullable=False, unique=False)
    name = db.Column(db.String(10), nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.uid'), unique=True)


class Sbom(db.Model):
    sbom_id = db.Column(db.Integer, primary_key=True)
    # sbom_name = db.Column(db.String(100), nullable=False, unique=False)
    date = db.Column(db.String(30), nullable=False, default=db.func.now())
    file = db.Column(db.String(), nullable=False, unique=False)
    latest=db.Column(db.String(), nullable=False, unique=False)
    



def add_sbom_data_from_json(json_data,updates):
    # Parse the JSON data into a Python dictionary
    data = json.loads(json_data)

    # Create a new Sbom instance and set its attributes
    sbom = Sbom(
        # sbom_name=data['sbom_name'],
        date=data['metadata']['timestamp'],
        file = json_data,
        latest=f"{updates}",
        
        
    )

    # Add the new Sbom instance to the session
    db.session.add(sbom)

    # Commit the session to the database
    db.session.commit()