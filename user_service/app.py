from flask import Flask, jsonify, request

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Danh sách người dùng (giả lập dữ liệu)
users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "Jane"}
]

# API: Lấy danh sách người dùng
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# API: Thêm người dùng mới
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    if any(user['id'] == new_user['id'] for user in users):
        return jsonify({"message": "User ID already exists!"}), 400
    users.append(new_user)
    return jsonify({"message": "User added successfully!", "user": new_user}), 201

# Chạy ứng dụng
if __name__ == '__main__':
    app.run(debug=True, port=5001)