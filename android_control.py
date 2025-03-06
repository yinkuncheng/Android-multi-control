import subprocess
import time
import os

class AndroidController:
    def __init__(self):
        """初始化控制器"""
        self.adb_path = "adb"  # 确保ADB已经添加到系统环境变量
        self.connected_devices = []

    def check_adb_installed(self):
        """检查ADB是否已安装"""
        try:
            subprocess.run([self.adb_path, "version"], capture_output=True, text=True)
            return True
        except FileNotFoundError:
            print("错误：未找到ADB。请确保已安装Android SDK并将ADB添加到系统环境变量。")
            return False

    def get_connected_devices(self):
        """获取已连接的设备列表"""
        result = subprocess.run([self.adb_path, "devices"], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')[1:]  # 跳过第一行（标题行）
        devices = []
        for line in lines:
            if line.strip():
                device_id = line.split('\t')[0]
                devices.append(device_id)
        self.connected_devices = devices
        return devices

    def connect_wireless(self, ip_address, port="5555"):
        """通过无线方式连接设备"""
        try:
            # 先断开可能的连接
            subprocess.run([self.adb_path, "disconnect", f"{ip_address}:{port}"])
            # 尝试连接
            result = subprocess.run(
                [self.adb_path, "connect", f"{ip_address}:{port}"],
                capture_output=True,
                text=True
            )
            print(result.stdout)
            return "connected" in result.stdout.lower()
        except Exception as e:
            print(f"连接失败：{str(e)}")
            return False

    def take_screenshot(self, device_id, save_path="screenshot.png"):
        """获取设备截图"""
        try:
            # 在设备上截图
            subprocess.run([self.adb_path, "-s", device_id, "shell", "screencap", "/sdcard/screen.png"])
            # 将截图拉取到电脑
            subprocess.run([self.adb_path, "-s", device_id, "pull", "/sdcard/screen.png", save_path])
            # 删除设备上的临时文件
            subprocess.run([self.adb_path, "-s", device_id, "shell", "rm", "/sdcard/screen.png"])
            return True
        except Exception as e:
            print(f"截图失败：{str(e)}")
            return False

    def tap_screen(self, device_id, x, y):
        """模拟点击屏幕"""
        try:
            subprocess.run([self.adb_path, "-s", device_id, "shell", "input", "tap", str(x), str(y)])
            return True
        except Exception as e:
            print(f"点击失败：{str(e)}")
            return False

    def swipe_screen(self, device_id, start_x, start_y, end_x, end_y, duration_ms=100):
        """模拟滑动屏幕"""
        try:
            subprocess.run([
                self.adb_path, "-s", device_id, "shell", "input", "swipe",
                str(start_x), str(start_y), str(end_x), str(end_y), str(duration_ms)
            ])
            return True
        except Exception as e:
            print(f"滑动失败：{str(e)}")
            return False

def main():
    # 创建控制器实例
    controller = AndroidController()

    # 检查ADB是否已安装
    if not controller.check_adb_installed():
        return

    # 获取已连接设备
    devices = controller.get_connected_devices()
    if not devices:
        print("未找到已连接的设备")
        return

    print("已连接的设备：")
    for i, device in enumerate(devices):
        print(f"{i + 1}. {device}")

    # 选择要控制的设备
    device_id = devices[0]  # 这里简单地选择第一个设备

    # 演示基本操作
    print("\n执行基本操作示例：")
    
    # 截图
    print("正在截图...")
    if controller.take_screenshot(device_id):
        print("截图成功，已保存为 screenshot.png")

    # 点击屏幕中心
    print("点击屏幕中心...")
    controller.tap_screen(device_id, 500, 500)  # 假设屏幕分辨率大于1000x1000

    # 向上滑动
    print("向上滑动...")
    controller.swipe_screen(device_id, 500, 800, 500, 200)

if __name__ == "__main__":
    main() 