from flask import Flask, render_template_string, url_for, request, jsonify, abort
from data import BOOKS

app = Flask(__name__)


def count_total_books():
    return len(BOOKS)


def count_available_books():
    return sum(1 for b in BOOKS if b["available"])


@app.context_processor
def inject_menu():
    def menu():
        return render_template_string(
            '<nav><a href="{{ url_for("index") }}">Trang chủ</a> | '
            '<a href="{{ url_for("books_list") }}">Danh sách sách</a></nav><hr>'
        )
    return dict(menu=menu)


@app.route("/")
def index():
    return render_template_string("""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Trang chủ</title></head>
<body>
{{ menu()|safe }}
<h1>Thư viện</h1>
<p>Tổng số đầu sách: {{ total }}</p>
<p>Sách sẵn sàng cho mượn: {{ available }}</p>
</body>
</html>""",
        total=count_total_books(),
        available=count_available_books(),
    )


@app.route("/books")
def books_list():
    category_filter = request.args.get("category")
    categories = sorted({b["category"] for b in BOOKS})
    books = [b for b in BOOKS if not category_filter or b["category"] == category_filter]
    return render_template_string("""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Danh sách sách</title></head>
<body>
{{ menu()|safe }}
<h1>Danh sách sách</h1>
<form method="get">
    <label>Thể loại:
        <select name="category" onchange="this.form.submit()">
            <option value="">Tất cả</option>
            {% for c in categories %}
            <option value="{{ c }}"{% if c == category_filter %} selected{% endif %}>{{ c }}</option>
            {% endfor %}
        </select>
    </label>
</form>
<table border="1" cellpadding="5">
<thead><tr><th>ID</th><th>Tên sách</th><th>Tác giả</th><th>Năm</th><th>Thể loại</th><th>Có sẵn</th></tr></thead>
<tbody>
{% for b in books %}
<tr>
<td>{{ b.id }}</td>
<td><a href="{{ url_for('book_detail', book_id=b.id) }}">{{ b.title }}</a></td>
<td>{{ b.author }}</td>
<td>{{ b.year }}</td>
<td>{{ b.category }}</td>
<td>{{ "Có" if b.available else "Không" }}</td>
</tr>
{% endfor %}
</tbody>
</table>
</body>
</html>""",
        books=books,
        categories=categories,
        category_filter=category_filter,
    )


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book is None:
        abort(404, description="Không có sách với ID = {}".format(book_id))
    return render_template_string("""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>{{ book.title }}</title></head>
<body>
{{ menu()|safe }}
<h1>{{ book.title }}</h1>
<p>Tác giả: {{ book.author }}</p>
<p>Năm: {{ book.year }}</p>
<p>Thể loại: {{ book.category }}</p>
<p>Có sẵn: {{ "Có" if book.available else "Không" }}</p>
<p><a href="{{ url_for('books_list') }}">Quay lại</a></p>
</body>
</html>""", book=book)


@app.route("/api/books")
def api_books():
    return jsonify(BOOKS)


@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if book is None:
        return jsonify({"error": "Không có sách với ID = {}".format(book_id)}), 404
    return jsonify(book)


@app.errorhandler(404)
def not_found(e):
    description = e.description if hasattr(e, "description") else "Không tìm thấy"
    return render_template_string("""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>404</title></head>
<body>
{{ menu()|safe }}
<h1>404 - Không tìm thấy</h1>
<p>{{ description }}</p>
<p><a href="{{ url_for('index') }}">Về trang chủ</a></p>
</body>
</html>""", description=description), 404


if __name__ == "__main__":
    app.run(debug=True)
