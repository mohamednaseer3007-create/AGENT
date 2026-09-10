import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from app.gmail import(
    is_email_command,
    extract_email,
    create_gmail_url,
    generate_email_with_gemini
)

from app.youtube import youtube_bp

def create_app():

    app = flask(__name__)
    CORS(app)


app.register_blueprint(
    youtube_bp,
    url_prefix="/youtube"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/html")
def html():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "ok"
        "service": "Nova AI Agent"
    })


@app.route("/agent", methods=["post"])
def agent():

    try:
        data = request.get_jsonify({
            "success": False,
            "message": "command is required"
        }), 400

if not is email_command(command):
    return jsonify({
        "success": False,
        "message": "please give a gmail command."
    }), 400

recipient = exact_email(command)

email = generate_email_with_gemini(command)

return jsonify({
    "susses": True,
    "type": "email",
    "email_generated": True,
    "recipient": recipient,
    "subject": email["subject"],
    "body":email["body"],
    "gmail_url": create_gmail_url(
        email["subject"],
        email["body"]'
        recipient
    )
})

except Exception as e:

    return jsonify({
        "success": False,
        "message": str(e)
    }), 500
return app
