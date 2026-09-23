from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    a_str = request.form.get("a")
    b_str = request.form.get("b")

    # Chưa có tham số → chỉ hiện form
    if a_str is None:
        return render_template("math.html")

    # Có tham số → gán 0 nếu rỗng, rồi tính
    a = float(a_str or 0)
    b = float(b_str or 0)

    def fmt(n):
        if n == int(n):
            return str(int(n))
        return f"{n:.6g}"

    results = [
        ("Tổng",     "A + B", fmt(a + b),                    False),
        ("Hiệu",     "A - B", fmt(a - b),                    False),
        ("Tích",     "A × B", fmt(a * b),                    False),
        ("Thương",   "A ÷ B", fmt(a / b) if b else "Lỗi chia 0", b == 0),
        ("Số dư",    "A % B", fmt(a % b) if b else "Lỗi chia 0", b == 0),
        ("Luỹ thừa", "A ^ B", fmt(a ** b),                   False),
    ]

    return render_template("math.html", a=a, b=b, results=results)


if __name__ == "__main__":
    app.run(debug=True)
