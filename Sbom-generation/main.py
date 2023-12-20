from operator import index
from flask import Flask, abort, jsonify, request, send_file
from main_flow import main_workflow
import json
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask_jwt_extended import current_user
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask import render_template
from flask_cors import CORS
from datetime import timedelta
# from app import convert_json_to_pdf
app = Flask(__name__)
from database.db_connect import db
from database.db_connect import Sbom, User, Role



CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}},
     headers=['Content-Type', 'Authorization'])
api = Api(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sql.sqlite3"
app.secret_key = "a6d058d1c0f72f09cccceb38bf9f8a7d"

app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json"]
app.config['JWT_SECRET_KEY'] = "2249aeaf3741da0431606da44f7976b0e9a6b7feb576bf4de098bd7ca0bb6a1f"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

db.init_app(app)
app.app_context().push()

# .....................................................................

# class User(db.Model):
#     uid = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(12), nullable=False, unique=False)
#     email = db.Column(db.String(40), nullable=False, unique=True)
#     last_login = db.Column(db.DateTime, nullable=True)
#     status = db.Column(db.String(10), nullable=False, default='unactive')
#     roles = db.relationship('Role', backref='user', uselist=False)


# class Role(db.Model):
#     rid = db.Column(db.Integer, primary_key=True, nullable=False, unique=False)
#     name = db.Column(db.String(10), nullable=False, unique=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.uid'), unique=True)




# def init_db():
    # with app.app_context():
    #     db.create_all()
def init_db():
    try:
        User.query.get(1)
    except:
         with app.app_context():
            db.create_all()
            # put one entry for admin in the database
            admin1 = User(username='admin1', password='admin@123',
                        email='ayushkumar@gmail.com', status='active')
            admin1.roles = Role(name='admin')

            # add and then commit to apply changes
            db.session.add(admin1)
            db.session.commit()
# .......................................................................

def role_required(required_roles):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            user_roles = get_jwt()['role']

            for role in required_roles:
                if role == user_roles:
                    return fn(*args, **kwargs)

            return jsonify(msg='Permission denied'), 403  # Forbidden

        return wrapper
    return decorator

# .......................................................................






class login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username, status='active').first()
        if user:
            if user.password == password:
                access_token = create_access_token(identity=user.uid, additional_claims={'role': user.roles.name})
                response = {'msg': 'Sign-in successful! Welcome user', 'user': username, 'role': user.roles.name, 'access_token': access_token}
                user.last_login = db.func.now()
                db.session.commit()
                return response
            else:
                return {'msg': 'Sign-in failed! Please check your credentials'}, 401
        else:
            return {'msg': 'User does not exist with username'}, 400


api.add_resource(login, '/api/login')


class logout(Resource):
    def post(self):
        try:
            response = jsonify({"msg": "Logout successful!"})
            return response
        except:
            return jsonify({"msg": "Something went wrong!"}), 500


api.add_resource(logout, '/api/logout')

    
class process_link(Resource):
    # @role_required(['admin'])
    def post(self):
        link = request.get_json()['link']
        user_id = "admin1"
        data, updates = main_workflow(link)
        
        info = json.loads(data)

        metadata = info['metadata']['timestamp']
        
        components = info.get('components', None)
        dependencies = []
        if components:
            for index, component in enumerate(components):
                dependency = {
                    'name': component['name'],
                    'version': component['version'],
                    'updates': updates[index],
                    
                }
                dependencies.append(dependency)
            return jsonify({
                'metadata': metadata,
                'dependencies': dependencies,
            })
        else:
            print("No 'components' key in the dictionary")
            time_stamp = {"Timestamp": metadata}
        
api.add_resource(process_link, '/api/process_link')

    
class fetch_all_sbom(Resource):
    # @role_required(['manager'])
    def get(self):

        sbom_data = Sbom.query.all() 
        data = [
            {
                'sbom_id': sbom.sbom_id,
                'date': sbom.date,
                
            }
            for sbom in sbom_data
        ]
        return jsonify(data)

api.add_resource(fetch_all_sbom, '/api/fetch_all_sbom')

class fetch_by_id(Resource):
    # @role_required(['manager'])
    def post(self):
        sbom_id=request.json['sbom_id']
        # Query the SbomData model
        sbom_data = Sbom.query.filter_by(sbom_id=sbom_id).first()

        # Convert the data to a format that can be JSONified
        file_data=json.loads(sbom_data.file)
        
        return jsonify(file_data['components'],sbom_data.latest)

api.add_resource(fetch_by_id, '/api/fetch_by_id')

class download_nontechnicl(Resource):
    # @role_required(['manager'])
    def get(self):
        sbom_id=request.json['sbom_id']
        # Query the SbomData model
        sbom_data = Sbom.query.filter_by(sbom_id=sbom_id).first()

        # Convert the data to a format that can be JSONified
        file_data=json.loads(sbom_data.file)
        
        return jsonify(file_data['components'],sbom_data.latest)

api.add_resource(download_nontechnicl, '/api/download_nontechnicl')


class download_technical(Resource):
    # @role_required(['manager'])
    def post(self):
        sbom_id=request.json['sbom_id']
        # Query the SbomData model
        # sbom_data = Sbom.query.filter_by(sbom_id=sbom_id).first()
        # file_data=json.loads(sbom_data.file)
        # Convert the data to a format that can be JSONified
        # with open('sbom.json', 'w') as f:
        #  json.dump(file_data['components'], f)

    # Send the file to the client
        return send_file('sbom.json', as_attachment=True)

api.add_resource(download_technical, '/api/download_technical')

# class download_pdf(Resource):
#     def get(self):
#         convert_json_to_pdf('sbom output.json', 'output.pdf')
#         return jsonify("success")

# api.add_resource(download_pdf, '/api/download_pdf')


if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0',port=5000)