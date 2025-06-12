# Ứng Dụng Chuyển File với Chữ Ký Số

Đây là một ứng dụng web cho phép chuyển file an toàn với khả năng ký số và xác thực file bằng thuật toán RSA. Ứng dụng giúp đảm bảo tính toàn vẹn và xác thực của các file được chuyển giao.

## Tính Năng Chính

- Tạo và quản lý cặp khóa RSA (khóa công khai và khóa riêng tư)
- Ký số file với khóa riêng tư
- Xác thực tính xác thực của file bằng khóa công khai
- Giao diện web trực quan, dễ sử dụng
- Tải xuống file đã ký và chữ ký số

## Yêu Cầu Hệ Thống

- Python 3.x trở lên
- Hệ điều hành: Windows/Linux/MacOS
- Trình duyệt web (Chrome, Firefox, Edge)

## Công Nghệ Sử Dụng

- Python 3.x
- Flask - Framework web
- Thư viện Cryptography cho RSA
- HTML/CSS/JavaScript cho giao diện

## Hướng Dẫn Cài Đặt

1. Tải mã nguồn về máy:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Tạo môi trường ảo Python:
```bash
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Cách Sử Dụng

1. Khởi động máy chủ:
```bash
python app.py
```

2. Mở trình duyệt và truy cập:
```
http://localhost:5000
```

3. Các bước thực hiện:

   a. Tạo cặp khóa:
   - Nhấn nút "Generate Keys" để tạo cặp khóa mới
   - Hệ thống sẽ tự động tạo và lưu khóa công khai và khóa riêng tư

   b. Ký số file:
   - Chọn file cần ký số
   - Nhấn nút "Upload & Sign"
   - Hệ thống sẽ tạo chữ ký số cho file
   - Tải xuống file đã ký và chữ ký số

   c. Xác thực file:
   - Tải lên file cần xác thực
   - Tải lên file chữ ký số tương ứng
   - Nhấn nút "Verify"
   - Hệ thống sẽ kiểm tra và thông báo kết quả xác thực

## Cấu Trúc Thư Mục

```
├── app.py                 # File chính của ứng dụng Flask
├── digital_signature.py   # Module xử lý chữ ký số
├── requirements.txt       # Danh sách thư viện cần thiết
├── templates/            # Thư mục chứa giao diện
│   └── index.html       # Trang chủ ứng dụng
└── uploads/             # Thư mục lưu file tạm
```

## Bảo Mật

- Sử dụng cặp khóa RSA 2048-bit
- Hàm băm SHA-256 cho chữ ký số
- Sử dụng padding PSS
- Xử lý file an toàn
- Bảo vệ khóa riêng tư
- Kiểm tra tính toàn vẹn file

## Lưu Ý Quan Trọng

- Bảo vệ khóa riêng tư cẩn thận
- Không chia sẻ khóa riêng tư với người khác
- Nên sao lưu cặp khóa ở nơi an toàn
- Luôn kiểm tra tính xác thực của file trước khi sử dụng

## Hỗ Trợ

Nếu bạn gặp vấn đề hoặc có thắc mắc, vui lòng:
- Tạo issue trong repository
- Liên hệ với tôi qua email
- Kiểm tra tài liệu hướng dẫn
