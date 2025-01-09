from flask import Flask, jsonify, request


# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Danh sách sản phẩm (giả lập dữ liệu)
products = [
    {"id": 101, "name": "Laptop"},
    {"id": 102, "name": "Phone"}
]


# API: Lấy danh sách sản phẩm
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# API: Thêm sản phẩm mới
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    if any(product['id'] == new_product['id'] for product in products):
        return jsonify({"message": "Product ID already exists!"}), 400
    products.append(new_product)
    return jsonify(
        {"message": "Product added successfully!", "product": new_product}
    ), 201


# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True, port=5002)
