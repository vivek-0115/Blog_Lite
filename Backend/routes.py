from flask import current_app as app, jsonify, request
from Backend.models import db
from flask_security import current_user, auth_required, hash_password, roles_required, verify_password

datastore = app.security.datastore

@app.route('/')
def home():
    return '<h1>Home Page.</h1>'

@app.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    email=data.get('email')
    password=data.get('password')

    if not email or not password:
        return jsonify({
                "message":"Invalid Request!"
            }), 404
    
    user=datastore.find_user(email=email)

    if not user:
        return jsonify({
            "message":"Invalid Email!"
        }),404
    if verify_password(password, user.password):
        return jsonify({
            "token":user.get_auth_token(),
            "email":user.email,
            "role":user.roles[0].name,
            "id":user.id}),200
    
    return jsonify({"message":"Invalid Password!"}),404

@app.route('/register', methods=['POST'])
def register():
    data=request.get_json()
    email=data.get('email')
    password=data.get('password')
    role=(data.get('role')).capitalize()

    if not email or not password or not role:
        return jsonify({"message":"Invalid Request!"}), 404
    
    user=datastore.find_user(email=email)

    if user:
        return jsonify({"message":"User Already Exist!"}),404
    
    try:   
        user=datastore.create_user(email=email,password=hash_password(password), roles=[role])
        db.session.commit()
        return jsonify({"message": "User Created", "user_id": user.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error While Creating", "error": str(e)}), 500

@app.route('/dashboard')
@auth_required()
@roles_required("Admin")
def admin_dash():
    return {
        "message":"Logged in Successfully",
        "email":current_user.email,
        "password":current_user.password,
        "active":current_user.active,
        "status_code":200
    }