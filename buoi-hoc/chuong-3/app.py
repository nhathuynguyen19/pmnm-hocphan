from flask import Flask, request as req, url_for
from data import POSTS

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return '<a href="/home">Home</a><br><a href="/gioi-thieu">Giới thiệu</a><br/><a href="/square/5.0">Square</a>'

@app.route('/gioi-thieu')
@app.route('/about')
def about():
    return 'Xin chào, đây là trang giới thiệu của chúng tôi.'

@app.route('/user/<username>')
def user_profile(username):
    return f'Xin chào, đây là trang cá nhân của {username}.'

@app.route('/square/<float:x>')
def square(x):
    return f'{x} * {x} = {x * x}'

@app.route('/square2/<x>')
def square2(x):
    return f'float({x}) * float({x}) = {float(x) * float(x)}'

@app.route('/sum/<strs>')
def tong(strs):
    # 1, 2, 3 = 6
    numbers = strs.split(',')
    total = sum(float(num) for num in numbers)
    return str(total)

@app.route('/tinh-toan')
def tinh_toan():
    a = req.args.get('a', type=float)
    b = req.args.get('b', type=float)
    op = req.args.get('op')

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        result = a / b
    else:
        return 'Toan tu khong hop le'

    return f'Kết quả: {result}'
def layout(title, body):
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <nav>
        <a href="{url_for('index')}">Trang chủ</a>
        <a href="{url_for('about')}">Giới thiệu</a>
        <a href="{url_for('search')}">Tìm kiếm</a>
    </nav>
    {body}
</body>
</html>"""

def find_post(post_id):
    for post in POSTS:
        if post["id"] == post_id:
            return post
    return None

if __name__ == '__main__':
    app.run(debug=True)
