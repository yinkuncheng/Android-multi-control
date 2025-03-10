# 安卓手机远程控制工具

这是一个使用 Python 实现的安卓手机远程控制工具，可以实现基本的一机多控功能。

## 功能特点

- 支持多设备连接和管理
- 支持无线连接（通过 ADB over WiFi）
- 支持基本操作：
  - 屏幕截图
  - 触摸控制（点击、滑动）
  - 按键模拟
  - 文件传输

## 使用前提

1. 安装 Android SDK（或至少安装 ADB 工具）
2. 将 ADB 添加到系统环境变量
3. 在目标手机上启用 USB 调试模式
4. 安装必要的 Python 包

## 安装步骤

1. 克隆或下载本项目
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. USB 连接方式：
   - 用 USB 线连接手机到电脑
   - 在手机上允许 USB 调试
   - 运行程序：
     ```bash
     python android_control.py
     ```

2. 无线连接方式：
   - 确保手机和电脑在同一个 WiFi 网络
   - 先用 USB 连接手机，开启 ADB 无线调试
   - 获取手机 IP 地址
   - 修改代码中的 IP 地址和端口
   - 运行程序

## 注意事项

1. 需要手机开启 USB 调试模式
2. 部分功能可能需要 Root 权限
3. 不同手机型号可能需要不同的权限设置
4. 建议在测试手机上使用，不要在主力机上使用

## 常见问题

1. 找不到设备
   - 检查 USB 连接
   - 确认已启用 USB 调试
   - 检查驱动是否正确安装

2. 无法执行操作
   - 检查权限设置
   - 确认手机是否已解锁
   - 查看是否需要 Root 权限

## 开发计划

- [ ] 添加图形用户界面
- [ ] 支持更多控制功能
- [ ] 添加设备管理功能
- [ ] 实现多设备并行控制
- [ ] 添加宏录制和回放功能
