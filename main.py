from flask import Flask, render_template
import requests
from post import Post

contents_url = "https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(contents_url).json()

post_sections = []

for post in posts:
    section = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_sections.append(section)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_sections)


@app.route('/post/<int:num>')
def post(num):
    requested_post = None
    for blog_post in post_sections:
        if blog_post.id == num:
            requested_post = blog_post

    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
