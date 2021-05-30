from flask import Flask, render_template, request
from post import Post
from dotenv import dotenv_values  # From address and password is held in a .env file in the working directory
from email.message import EmailMessage
import requests
import smtplib


MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "587"
CONFIG = dotenv_values(".env")

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["date"], post["author"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_root_page():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    to = CONFIG["TO"]
    body = f"{name} wants to talk... \n\n Email: {email} \n\n Phone: {phone} \n\n {message} "
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Message From Blog"
    msg['From'] = CONFIG["FROM"]
    msg['To'] = to

    with smtplib.SMTP(MAIL_SERVER, port=MAIL_PORT) as mail:
        mail.starttls()
        mail.login(user=CONFIG["FROM"], password=CONFIG["PASSWORD"])
        mail.send_message(msg)


if __name__ == "__main__":
    app.run()


