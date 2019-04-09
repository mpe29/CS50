from flask import Flask, render_template
import time
app = Flask(__name__)

x=time.perf_counter()
print(x)
@app.route("/")
def index():
    x=time.asctime()
    headline = f"Hello, world! The time is: {x}"
    return render_template("index.html", headline=headline,time=x)
    print(x)
