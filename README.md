# Ứng Dụng Chuyển File với Chữ Ký Số RSA (Mô Hình Máy Chủ Tập Trung)

Đây là một ứng dụng web cho phép ký số và xác thực file bằng thuật toán RSA, được triển khai trên một máy chủ trung tâm. Ứng dụng giúp đảm bảo tính toàn vẹn và xác thực của các file được chuyển giao giữa các bên khác nhau mà không cần truyền tải file trực tiếp giữa các máy trạm.

## Tính Năng Chính

- Tạo và quản lý cặp khóa RSA (khóa công khai và khóa riêng tư) gắn với một tên người dùng (username).
- Ký số file với khóa riêng tư và lưu trữ file gốc cùng chữ ký số trên máy chủ.
- Xác thực tính xác thực của file bằng khóa công khai trên máy chủ, dựa trên tên file và tên người dùng.
- Giao diện web trực quan, dễ sử dụng với thanh tiến độ.

## Yêu Cầu Hệ Thống

- Python 3.x trở lên
- Hệ điều hành: Windows/Linux/MacOS (cho máy chủ và các máy trạm)
- Trình duyệt web hiện đại (Chrome, Firefox, Edge)

## Công Nghệ Sử Dụng

- Python 3.x
- Flask - Framework web
- Thư viện Cryptography cho RSA
- HTML/CSS/JavaScript cho giao diện

## Hướng Dẫn Cài Đặt

1.  Tải mã nguồn về máy (trên máy chủ trung tâm):
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  Tạo môi trường ảo Python:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
    ```

3.  Cài đặt các thư viện cần thiết:
    ```bash
    pip install -r requirements.txt
    ```

## Cách Sử Dụng (Mô Hình Máy Chủ Tập Trung)

Để sử dụng ứng dụng này giữa hai máy tính khác nhau (hoặc nhiều hơn), bạn cần có một **máy chủ trung tâm duy nhất** chạy ứng dụng Flask. Các máy tính khác sẽ truy cập vào máy chủ này.

1.  **Khởi động máy chủ trung tâm:**

    *   **Trên máy chủ trung tâm:** Mở terminal, điều hướng đến thư mục dự án và chạy lệnh sau:
        ```bash
        python app.py
        ```
    *   Lưu ý: Ứng dụng sẽ chạy trên `http://0.0.0.0:5000/`, cho phép các máy khác trong cùng mạng truy cập được.

2.  **Truy cập ứng dụng từ các máy trạm:**

    *   **Từ máy của Người gửi và Người nhận:** Mở trình duyệt web và truy cập vào địa chỉ IP của máy chủ trung tâm (ví dụ: `http://192.168.1.100:5000`).

3.  **Quy trình thực hiện:**

    **a. Dành cho Người gửi:**
    *   Truy cập trang gửi: `http://<Địa_chỉ_IP_máy_chủ>:5000/sender`
    *   **Bước 1: Tạo Cặp Khóa:**
        *   Nhập một **Tên người dùng (Username)** của bạn (ví dụ: `nguoigui_alice`). Đây sẽ là định danh của bạn khi trao đổi file.
        *   Nhấn nút **"Tạo Cặp Khóa"**. Hệ thống sẽ tạo cặp khóa RSA và lưu chúng trên máy chủ trung tâm (`nguoigui_alice_private_key.pem`, `nguoigui_alice_public_key.pem`).
    *   **Bước 2: Ký Số File:**
        *   Chọn file cần ký số từ máy tính của bạn.
        *   Nhấn nút **"Ký Số & Tải Xuống"**. File gốc và chữ ký số (`.sig`) sẽ được lưu trữ trên máy chủ trung tâm.
        *   Sau khi ký thành công, giao diện sẽ hiển thị thông tin cần thiết: **Tên file gốc**, **Tên file chữ ký**, và **Tên người dùng (username)** của bạn. **Người gửi cần cung cấp BA thông tin này cho người nhận thông qua một kênh liên lạc riêng (ví dụ: email, tin nhắn, gọi điện).**

    **b. Dành cho Người nhận:**
    *   Truy cập trang nhận: `http://<Địa_chỉ_IP_máy_chủ>:5000/receiver`
    *   **Bước 1: Nhập Thông Tin File:**
        *   Nhập **Tên file cần xác thực** (là tên file gốc mà người gửi đã cung cấp, ví dụ: `document.docx`).
        *   Nhập **Tên file chữ ký số** (là tên file chữ ký mà người gửi đã cung cấp, ví dụ: `document.docx.sig`).
        *   Nhập **Tên người dùng của người gửi** (là username mà người gửi đã cung cấp, ví dụ: `nguoigui_alice`).
        *   Nhấn nút **"Kiểm tra thông tin"** để chuyển sang bước xác thực.
    *   **Bước 2: Xác Thực:**
        *   Nhấn nút **"Xác Thực"**. Máy chủ trung tâm sẽ tự động tìm các file trên (`document.docx`, `document.docx.sig`, `nguoigui_alice_public_key.pem`) và tiến hành xác thực.
        *   Kết quả xác thực (Hợp lệ / Không hợp lệ) sẽ được hiển thị trên giao diện.

## Cấu Trúc Thư Mục

```
├── app.py                 # File chính của ứng dụng Flask (máy chủ)
├── digital_signature.py   # Module xử lý chữ ký số
├── requirements.txt       # Danh sách thư viện cần thiết
├── templates/            # Thư mục chứa giao diện HTML
│   ├── index.html       # (Nếu có trang mặc định)
│   ├── sender.html      # Trang người gửi
│   └── receiver.html    # Trang người nhận
├── static/               # Thư mục chứa các file CSS, JavaScript
│   └── style.css        # File CSS cho giao diện
└── uploads/             # Thư mục lưu trữ file tạm (file gốc, chữ ký, khóa)
```

## Bảo Mật

- Sử dụng cặp khóa RSA 2048-bit.
- Hàm băm SHA-256 cho chữ ký số.
- Sử dụng padding PSS.
- Xử lý file an toàn trên máy chủ.

## Lưu Ý Quan Trọng

-   **Bảo vệ khóa riêng tư cẩn thận:** Khóa riêng tư (`[username]_private_key.pem`) nằm trên máy chủ. Đảm bảo máy chủ được bảo mật.
-   **Tin cậy khóa công khai:** Trong mô hình này, việc người gửi phải thông báo username và người nhận phải tin vào username đó là quan trọng. Trong thực tế, để giải quyết vấn đề tin cậy khóa công khai giữa các bên không quen biết, cần có một **Cơ sở hạ tầng Khóa công khai (PKI)** và **Tổ chức cấp chứng chỉ (CA)**, điều này vượt ra ngoài phạm vi của ứng dụng minh họa này.
-   Nếu gặp lỗi "Public key not found for this username", hãy đảm bảo người gửi đã tạo khóa thành công với đúng username đó trên máy chủ.
-   Nếu gặp lỗi "File not found on server" hoặc "Signature file not found on server", hãy đảm bảo người gửi đã ký file thành công và cung cấp đúng tên file cho người nhận.

## Hỗ Trợ

Nếu bạn gặp vấn đề hoặc có thắc mắc, vui lòng:
- Tạo issue trong repository
- Liên hệ với tôi qua email
- Kiểm tra tài liệu hướng dẫn 
