from flask import Flask

app=Flask(__name__)

@app.route("/")
  def index():
    names=["Alice","bob","charlie"]
    return render_template("index.html",names=names)
