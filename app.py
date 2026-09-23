from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("math.html")

    # POST
    a = float(request.form["a"])
    b = float(request.form["b"])
    return render_template("math.html",
                           a=a, b=b,
                           tong=a + b,
                           hieu=a - b,
                           tich=a * b,
                           thuong=a / b if b != 0 else "Lỗi chia 0")


if __name__ == "__main__":
    app.run(debug=True)
