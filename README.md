# Tool_farm_pass_tft
🤖 Tool Auto Cày Pass Đấu Trường Chân Lý (TFT)
Đây là công cụ tự động hóa giúp bạn treo máy cày Pass sự kiện của chế độ Đấu Trường Chân Lý (TFT). Tool hoạt động dựa trên cơ chế nhận diện hình ảnh và tự động mô phỏng thao tác chuột/phím để: Tự tìm trận ➡️ Chấp nhận ➡️ Đợi đến round 3.1 ➡️ Đầu hàng ➡️ Chơi lại vòng mới.

⚠️ CẢNH BÁO QUAN TRỌNG:
Việc sử dụng phần mềm tự động can thiệp vào game có rủi ro vi phạm điều khoản của Riot Games. Hệ thống Vanguard rất gắt gao. Vui lòng chỉ sử dụng ở tài khoản phụ và không treo tool liên tục 24/7 để tránh bị khóa tài khoản.

🛠️ Bước 1: Cài đặt môi trường (Dành cho người mới)
Máy tính của bạn cần có Python để chạy được tool này.

Tải Python: Truy cập trang chủ python.org/downloads và tải phiên bản mới nhất cho Windows.

Cài đặt Python: Mở file vừa tải về. RẤT QUAN TRỌNG: Bạn BẮT BUỘC phải tích vào ô "Add Python.exe to PATH" ở dưới cùng trước khi bấm Install Now.

Cài đặt thư viện: * Bấm phím Windows, gõ cmd.

Nhấp chuột phải vào Command Prompt và chọn "Run as administrator" (Chạy dưới quyền Quản trị viên).

Copy dòng lệnh dưới đây, dán vào CMD và nhấn Enter để cài đặt các "bộ não" nhận diện cho tool:

Bash
pip install pyautogui pydirectinput opencv-python pillow
📸 Bước 2: Chuẩn bị "Mắt thần" (Hình ảnh mẫu)
Tool cần biết các nút bấm trông như thế nào để click. Bạn cần vào game, chụp ảnh màn hình, cắt lấy các nút bấm và lưu vào cùng một thư mục với file code (pass.py).

Hãy lưu tên file chính xác 100% như danh sách dưới đây (định dạng .png):

play_button.png : Nút Tìm Trận ở sảnh.

accept_button.png : Nút Chấp Nhận trận đấu.

round_32_indicator.png : Vùng hiển thị số 3-2 ở giữa phía trên màn hình (Nên cắt rộng ra một chút, lấy cả viền xám xung quanh chữ).

ff_confirm.png : Nút Đầu Hàng (Nút màu đỏ hiện ra sau khi gõ /ff).

play_again_button.png : Nút Chơi Lại ở màn hình kết quả cuối trận.

⚙️ Bước 3: Cài đặt Game & Máy tính
Để tool không bị "mù" hoặc click trượt, bạn phải đảm bảo thiết lập như sau:

Độ thu phóng Windows: Ra ngoài Desktop, chuột phải chọn Display Settings. Ở mục Scale, bắt buộc phải để 100%.

Chế độ màn hình Game: Trong mục Cài đặt Hình ảnh của LMHT, đổi sang chế độ Cửa sổ (Windowed) hoặc Không viền (Borderless). Tuyệt đối không để Toàn màn hình (Fullscreen).

Độ phân giải: Khi bạn chụp các ảnh mẫu .png ở độ phân giải nào, thì lúc chạy tool game phải giữ nguyên độ phân giải đó.

🚀 Bước 4: Cách chạy Tool
Mở Command Prompt (CMD) dưới quyền Quản trị viên (Run as administrator).

Di chuyển đến thư mục chứa file code bằng lệnh cd.
(Ví dụ: Nếu bạn để thư mục tool ngoài Desktop, hãy gõ: cd Desktop\tool tft và nhấn Enter).

Khởi động tool bằng lệnh:

Bash
python pass.py
Để màn hình sảnh TFT ở ngay trước mặt và xem tool tự động làm việc!

🛑 Cách dừng Tool khẩn cấp
Nếu tool bị kẹt, click nhầm, hoặc bạn muốn dừng lại để chơi tay:

Cách 1: Quay lại cửa sổ CMD màu đen và nhấn tổ hợp phím Ctrl + C.

Cách 2 (Giật dây an toàn): Kéo thật mạnh chuột văng ra một trong 4 góc ngoài cùng của màn hình. Tính năng an toàn (Fail-Safe) sẽ lập tức văng lỗi và ép tool dừng lại hoàn toàn.

🐛 Các lỗi thường gặp
Báo lỗi ImageNotFoundException: Do thiếu ảnh trong thư mục, hoặc lưu sai tên, sai đuôi file (.jpg thay vì .png).

Game trơ ra không nhận phím/chuột: Do bạn chưa chạy CMD bằng quyền Run as administrator.

Tool gõ /ff nhưng nút Xác nhận không click được: Ảnh ff_confirm.png cắt chưa chuẩn. Hãy vào game tự gõ /ff và chụp lại ảnh cái nút đó thật rõ nét.

Bị văng ra sảnh nhưng tool vẫn đếm giờ: Không sao cả, tool đã được tích hợp cơ chế chống kẹt hàng chờ, nó sẽ tự động tìm trận mới ngay lập tức.

Nếu đến round 3.1 không tự ff thì chụp lại ảnh round_31_indicator rồi cắt sao cho chuẩn rõ nét.
