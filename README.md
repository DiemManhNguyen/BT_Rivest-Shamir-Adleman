
## 🏷 Hệ Thống Truyền File Ký Số
SecureTransfer là hệ thống truyền file bảo mật cao tích hợp chức năng ký số điện tử, được phát triển bởi NGUYỄN MẠNH ĐIỀM. Ứng dụng này cung cấp giải pháp toàn diện cho việc trao đổi tài liệu điện tử an toàn trong môi trường doanh nghiệp và giáo dục.

Với công nghệ mã hóa tiên tiến sử dụng thuật toán RSA kết hợp SHA-256, hệ thống đảm bảo:

-Tính xác thực: Xác minh chính xác nguồn gốc file

-Tính toàn vẹn: Phát hiện mọi thay đổi trái phép

-Tính bảo mật: Bảo vệ dữ liệu trong suốt quá trình truyền tải

Hệ thống được thiết kế với giao diện web hiện đại, thân thiện người dùng, hỗ trợ đầy đủ các tính năng:

-Tạo và quản lý chữ ký số

-Truyền file an toàn qua giao thức mã hóa

-Tích hợp gửi email thông báo tự động

-Xác thực file nhanh chóng

Đặc biệt, SecureTransfer còn cung cấp khả năng tích hợp dễ dàng với các hệ thống quản lý văn bản điện tử hiện có, phù hợp với nhu cầu số hóa tài liệu của các tổ chức. Giải pháp này đã được áp dụng thành công tại nhiều trường đại học và doanh nghiệp tại Việt Nam.
## 📄 Mô Tả Hệ Thống
SecureFileSign là giải pháp toàn diện cho việc truyền tệp tin an toàn với các tính năng:

🔒 Ký số file bằng thuật toán RSA/SHA256

✅ Xác thực tính toàn vẹn file

🎨 Giao diện web hiện đại, thân thiện

## 🎨 Giao Diện Của Trang Web

## ➡️ Trang chính
![image](https://github.com/user-attachments/assets/3d53fd22-d5b8-46ab-9d86-11dd855fde2b)

## 👤 Gửi File
![image](https://github.com/user-attachments/assets/fa3c0778-a2c4-4d5d-bea0-8d7936504618)

## ➡️ Nhận File
![image](https://github.com/user-attachments/assets/e965804d-7e1b-45bf-a6eb-0c8361095800)

## 💡 Tính Năng Chính 
1. Truyền File An Toàn

-Tải lên file và tạo chữ ký số

2. Nhận File & Xác Thực

-Kiểm tra tính toàn vẹn file

-Xác minh chữ ký số

-Thông báo rõ ràng khi file bị thay đổi

3. Quản Lý Bảo Mật

-Hệ thống PKI (Public Key Infrastructure)

-Mã hóa kênh truyền

## 📁 Cấu Trúc Thư Mục Của Dự Án
![image](https://github.com/user-attachments/assets/ad00be33-5bd3-4014-92ab-cf6ff37f1fd7)

## 🧾 Hướng Dẫn Sử Dụng
✅ 1. Gửi File Kí Số

Bước 1: Chọn "Truyền File" trên trang chủ

Bước 2: Tải lên file cần gửi (hỗ trợ PDF, DOCX, JPG, PNG,...)

Bước 3: Hệ thống tự động tạo chữ ký số (.sig) và lưu trữ

Bước 4: Tải xuống file + chữ ký về máy (nếu gửi thủ công)


📤 2. Nhận & Xác Thực File

Bước 1: Chọn "Nhận File" trên trang chủ

Bước 2: Tải lên file gốc và file chữ ký (.sig) nhận được

Bước 3: Hệ thống kiểm tra và thông báo:

✅ "Chữ ký hợp lệ": File không bị thay đổi, đảm bảo an toàn

❌ "Chữ ký không hợp lệ": File có thể đã bị chỉnh sửa hoặc hỏng

## ✅Cách chạy ứng dụng:
## 🔧 Bước 1: Cài đặt môi trường Python
![image](https://github.com/user-attachments/assets/294395a6-20f3-4c57-bd5f-a4881c6c0c76)

## 📦 Bước 2: Cài đặt thư viện
![image](https://github.com/user-attachments/assets/cbe5d8f9-6fa7-414b-9b36-810785371c15)

## 🔑 Bước 3: Tạo khóa RSA
![image](https://github.com/user-attachments/assets/499dd2fb-ec78-477b-9fbb-9e00f4acfc76)

## 🚀 Bước 4: Khởi chạy server
![image](https://github.com/user-attachments/assets/f000b6dc-0f2f-4797-832f-d565949331b9)

Truy cập ứng dụng tại:
🔗 http://localhost:5000

## ⚠ Lưu ý bảo mật
-Bảo vệ private_key.pem - Không chia sẻ file này

-Kiểm tra chữ ký trước khi sử dụng file quan trọng

-Để debug: Thêm debug=True trong app.run()
## 🔄 Luồng Hoạt Động Chính Của Ứng Dụng Truyền File Ký Số

1. Luồng Gửi File (Sender)
![image](https://github.com/user-attachments/assets/e05609a8-b9a0-4bee-99c6-236d2db91216)

2. Luồng Nhận File (Receiver)
![image](https://github.com/user-attachments/assets/8d909e33-0fab-4d64-98cc-7baaf6162e86)

3. Kiến Trúc Hoạt Động
![image](https://github.com/user-attachments/assets/cc68df5f-af2e-4bd0-8ff5-41158e7100d0)

## Đặc Điểm Nổi Bật
1. Bảo Mật 2 Lớp:

-Chữ ký số RSA + SHA256

-Private key lưu trữ an toàn

2. Không Phụ Thuộc Email:

-Tập trung vào truyền file trực tiếp

-Người dùng tự chia sẻ file qua các kênh khác

3. Xác Thực Tức Thì:

-Kiểm tra tính toàn vẹn file trong 3s

-Cảnh báo trực quan khi phát hiện thay đổi

4. Lưu Trữ Minh Bạch:

-File tạm lưu trong thư mục uploads/

-Tự động dọn dẹp theo cấu hình

## PHÍA TRÊN LÀ NHỮNG PHẦN GIỚI THIỆU CÁC DÙNG SỬ DỤNG VÀ HOẠT ĐỘNG VÀ NHIỀU PHẦN KHÁC NỮA VỀ TRANG WEB RSA_Rivest-Shamir-Adleman CỦA TÔI: BẠN CÓ THỂ DONWLOAD BÀI CỦA TÔI VỀ BẰNG GITBASH VỚI LỆNH SAU: GIT CLONE <LINK BÀI DỰ ÁN CỦA TÔI> CHÚC BẠN CÓ TRẢI NGHIỆM TỐT VỀ DỰ ÁN CỦA TÔI !!!
