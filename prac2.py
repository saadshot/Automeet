import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
print(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))