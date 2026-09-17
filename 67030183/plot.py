# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "matplotlib",
#     "numpy",
#     "scipy"
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np

# ข้อมูลจากการทดลองของนักศึกษา (Lab 6.2)
rssi = np.array([0, 0, -2, 1, 0])
throughput = np.array([346.13, 343.40, 1533.26, 840.42, 1433.03])

# เนื่องจากข้อมูล RSSI ของนักศึกษามีค่าเป็น 0 และค่าบวก จึงไม่สามารถทำ Logarithmic Regression (ln(-x)) ได้
# จึงขออนุญาตใช้ Linear Regression แทน เพื่อให้ออกมาในรูปแบบที่ใกล้เคียงกับภาพตัวอย่างที่สุด
slope, intercept = np.polyfit(rssi, throughput, 1)

# คำนวณ R-squared
p = np.poly1d([slope, intercept])
yhat = p(rssi)
ybar = np.sum(throughput)/len(throughput)
ssreg = np.sum((yhat-ybar)**2)
sstot = np.sum((throughput - ybar)**2)
r_squared = ssreg / sstot

# สร้างจุดสำหรับวาดเส้น
x_line = np.linspace(min(rssi)-1, max(rssi)+1, 100)
y_line = p(x_line)

# ตั้งค่าขนาดรูปภาพ
plt.figure(figsize=(8, 5))

# จุดข้อมูลจริง (สีน้ำเงิน)
plt.scatter(rssi, throughput, color='#2962FF', s=80, label='Measured data', zorder=5)

# เส้นสมการ (สีแดง)
eq_str = f"y = {slope:.2f}x + {intercept:.2f}\n$R^2$ = {r_squared:.4f}"
plt.plot(x_line, y_line, color='#D50000', linewidth=2, label=eq_str, zorder=4)

# ตั้งค่าหัวข้อและแกน
plt.title('RSSI vs Throughput — Linear Regression', fontsize=13)
plt.xlabel('RSSI (dBm)', fontsize=11)
plt.ylabel('Throughput (Kbps)', fontsize=11)

# ตั้งค่า Grid และ Legend แบบในรูป
plt.grid(True, linestyle='-', color='#E0E0E0', alpha=0.7, zorder=0)
plt.legend(loc='upper left', fontsize=10, framealpha=1.0, edgecolor='#CCCCCC')

# ปรับ Layout และเซฟรูป
plt.tight_layout()
plt.savefig('rssi_vs_throughput.png', dpi=300)
print("Plot saved to rssi_vs_throughput.png")
