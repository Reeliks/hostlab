from flask import Blueprint, request, render_template
from database import get_user_id_by_code, create_user_session

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def login_page():
    return render_template("login.j2")

@main_bp("/api/login", methods=["POST"])
def login(): 
    code = request.args.get("code")
    if not code:
        return "Code not provided", 401

    user_id = get_user_id_by_code(code)
    if not user_id:
        return "User with such code not found", 401
    
    ipv4_address = request.remote_addr
    user_agent = request.user_agent

    token = create_user_session(
        user_id=user_id, 
        ipv4_address=ipv4_address, 
        user_agent=user_agent
    )

    return {token: token}, 201
    
@main_bp.route("/lab")
def lab_page():
    return render_template("lab.j2")