from flask import Flask

app = Flask(__name__)

@app.route("/hello/")
#http://127.0.0.1:5000/hello/FamosoPvP
@app.route("/hello/<nome>")
def hello(nome=""):
    return f"<h1>Hello {nome}<h1>"

@app.route("/blog/")
@app.route("/blog/<int:postID>")
def blog(postID=-1):
    if postID >= 0:
        return f"blog info {postID}"
    else:
        return "blog todo"

@app.route("/blog/<float:postID>")
def blog2(postID=-1):
    if postID >= 0:
        return f"blog float {postID}"
    else:
        return "blog float todo"


if __name__ == "__main__":
    app.run(debug=True)

