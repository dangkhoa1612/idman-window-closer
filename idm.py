import time
import threading
import win32gui
import win32process
import psutil
import win32con
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

class IDManWindowCloser:
    def __init__(self):
        self.is_running = True
        self.icon = None

    def window_enum_handler(self, hwnd, result_list):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            rect = win32gui.GetWindowRect(hwnd)
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                process = psutil.Process(pid)
                exe_name = process.name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                exe_name = "<Unknown>"

            width = rect[2] - rect[0]
            height = rect[3] - rect[1]

            if exe_name.lower() == "idman.exe":
                print(f"{window_text} - {exe_name} Size {width}x{height}")


            if not window_text and exe_name.lower() == "idman.exe" and width > 246 and height > 346:
                result_list.append(hwnd)

    def close_windows(self):
        while True:
            if self.is_running:
                windows = []
                win32gui.EnumWindows(self.window_enum_handler, windows)
                for hwnd in windows:
                    try:
                        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                        print(f"Đã đóng cửa sổ có Handle: {hwnd}")
                    except Exception as e:
                        print(f"Không thể đóng cửa sổ có Handle: {hwnd}. Lỗi: {e}")
            time.sleep(1)

    def create_image(self, color):
        width, height = 64, 64
        image = Image.new('RGB', (width, height), color)
        dc = ImageDraw.Draw(image)
        dc.rectangle(
            (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
            fill='white'
        )
        return image

    def on_exit(self, icon, item):
        icon.stop()

    def toggle_pause(self, icon, item):
        # Thay đổi trạng thái "Pause" và "Play"
        self.is_running = not self.is_running
        # Cập nhật icon và tiêu đề
        icon.icon = self.create_image('green' if self.is_running else 'orange')
        icon.title = "IDMan Window Closer (Running)" if self.is_running else "IDMan Window Closer (Paused)"
        print(f"Trạng thái hiện tại: {'Đang chạy' if self.is_running else 'Tạm dừng'}")
        
        # Cập nhật menu với trạng thái mới
        self.update_menu(icon)

    def update_menu(self, icon):
        # Tạo lại menu với trạng thái mới cho nút Pause/Play
        pause_text = 'Pause' if self.is_running else 'Play'
        menu = Menu(
            MenuItem(pause_text, self.toggle_pause),
            MenuItem('Exit', self.on_exit)
        )
        icon.menu = menu

    def setup(self, icon):
        icon.visible = True

    def run_icon(self):
        # Khởi tạo menu với trạng thái ban đầu là Pause
        menu = Menu(
            MenuItem('Pause', self.toggle_pause),
            MenuItem('Exit', self.on_exit)
        )
        self.icon = Icon('IDMan Window Closer', self.create_image('green'), menu=menu)
        self.icon.title = "IDMan Window Closer (Running)"
        
        # Chạy icon
        self.icon.run(setup=self.setup)

    def run(self):
        # Chạy luồng đóng cửa sổ
        threading.Thread(target=self.close_windows, daemon=True).start()
        # Chạy icon
        self.run_icon()

if __name__ == "__main__":
    app = IDManWindowCloser()
    app.run()

# pyinstaller --onefile --noconsole idm.py
# pyinstaller --onefile --icon=youricon.ico idm.py
