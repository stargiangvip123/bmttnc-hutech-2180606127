from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)

# Khởi tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        # Nhận dữ liệu từ yêu cầu POST
        data = request.json
        plain_text = data['plain_text']
        key = int(data['key'])
        
        # Mã hóa văn bản
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        
        # Trả về kết quả dưới dạng JSON
        return jsonify({'encrypted_message': encrypted_text}), 200
    except Exception as e:
        # Báo lỗi nếu có lỗi xảy ra
        return jsonify({'error': str(e)}), 400

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        # Nhận dữ liệu từ yêu cầu POST
        data = request.json
        cipher_text = data['cipher_text']
        key = int(data['key'])
        
        # Giải mã văn bản
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        
        # Trả về kết quả dưới dạng JSON
        return jsonify({'decrypted_message': decrypted_text}), 200
    except Exception as e:
        # Báo lỗi nếu có lỗi xảy ra
        return jsonify({'error': str(e)}), 400

# Main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
