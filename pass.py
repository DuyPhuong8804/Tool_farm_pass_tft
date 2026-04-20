import pyautogui
import pydirectinput
import time
import random

# Độ chính xác chung cho các nút bấm
CONF = 0.85

def click_image(img_path, message):
    try:
        pos = pyautogui.locateOnScreen(img_path, confidence=CONF)
        if pos:
            point = pyautogui.center(pos)
            
            target_x = int(point.x + random.randint(-5, 5))
            target_y = int(point.y + random.randint(-5, 5))
            
            # 1. Di chuyển chuột đến nút
            pyautogui.moveTo(target_x, target_y)
            time.sleep(0.1) # Đợi game sáng viền nút lên (Hover state)
            
            # 2. Dùng pyautogui nhấn và giữ 0.15 giây
            pyautogui.mouseDown()
            time.sleep(0.15) # Thời gian vàng để game ghi nhận click
            pyautogui.mouseUp()
            
            print(f"[OK] {message}")
            return True
    except pyautogui.ImageNotFoundException:
        return False
    except Exception:
        return False
    return False

def is_image_visible(img_path, strict_conf=CONF):
    try:
        pos = pyautogui.locateOnScreen(img_path, confidence=strict_conf)
        return True if pos else False
    except:
        return False

def start_auto():
    print("--- Tool bắt đầu chạy ---")
    in_match = False
    match_start_time = 0

    while True:
        # ==========================================
        # ƯU TIÊN 1: XỬ LÝ HÀNG CHỜ VÀ BỊ HỦY TRẬN
        # ==========================================
        
        # 1. Luôn quét nút Chấp nhận trước
        if click_image('accept_button.png', "Đã nhấn Chấp nhận! Bắt đầu đếm giờ..."):
            in_match = True
            match_start_time = time.time() # Đặt lại đồng hồ đếm 8 phút
            time.sleep(8) # Đợi 8 giây cho bảng Accept biến mất hoặc game load
            continue # Quay lại đầu vòng lặp ngay để kiểm tra tiếp

        # 2. Nếu không có nút Chấp nhận, quét xem có bị văng ra sảnh không (thấy nút Tìm trận)
        if click_image('play_button.png', "Đang tìm trận..."):
            in_match = False # Đánh dấu là chưa vào game
            time.sleep(3)
            continue

        # ==========================================
        # ƯU TIÊN 2: KHI ĐÃ VÀO TRẬN (Đợi đến 3.1)
        # ==========================================
        if in_match:
            current_time = time.time()
            elapsed_time = current_time - match_start_time
            
            # Khóa 8 phút (480 giây)
            if elapsed_time > 480:
                if is_image_visible('round_31_indicator.png', strict_conf=0.95):
                    print("[INFO] Đã đến vòng 3.1. Tiến hành đầu hàng.")
                    
                    surrendered = False
                    while not surrendered:
                        pydirectinput.press('enter')
                        time.sleep(1)
                        
                        pydirectinput.press('/')
                        time.sleep(0.1)
                        pydirectinput.press('f')
                        time.sleep(0.1)
                        pydirectinput.press('f')
                        time.sleep(0.5)
                        pydirectinput.press('enter')
                        
                        print("Đang tìm nút xác nhận đầu hàng...")
                        time.sleep(2)
                        
                        if click_image('ff_confirm.png', "Đã click nút xác nhận!"):
                            time.sleep(1)
                            # Kiểm tra lại xem nút đã biến mất chưa
                            if not is_image_visible('ff_confirm.png'):
                                print("[THÀNH CÔNG] Game đã nhận lệnh đầu hàng!")
                                surrendered = True
                            else:
                                print("[LỖI] Click ảo, game chưa nhận, sẽ thử lại...")
                        else:
                            print("[CẢNH BÁO] Không thấy nút xác nhận, thử gõ lại lệnh /ff...")
                            pydirectinput.press('esc') 
                            time.sleep(2)
                    
                    # 3. ĐỢI RA SẢNH VÀ CHƠI LẠI
                    print("Đang đợi màn hình kết quả để nhấn Chơi lại...")
                    clicked_play_again = False
                    while not clicked_play_again:
                        if click_image('play_again_button.png', "Đã nhấn Chơi lại! Quay về sảnh..."):
                            clicked_play_again = True
                        else:
                            time.sleep(3)
                    
                    time.sleep(8) # Đợi Client load xong sảnh
                    print("--- Bắt đầu vòng lặp mới ---")
                    in_match = False # Kết thúc vòng đời trận đấu, trả về sảnh
            else:
                # Nếu chưa đủ 8 phút, in ra màn hình cho bạn biết tiến độ
                print(f"Đang trong trận / Đang load... Đã qua {int(elapsed_time)} giây (Cần đợi 480s)")
                time.sleep(5) # Cứ 5 giây vòng lặp check hàng chờ/thời gian 1 lần
        
        # Nghỉ siêu ngắn để CPU không bị quá tải
        time.sleep(1)

if __name__ == "__main__":
    start_auto()