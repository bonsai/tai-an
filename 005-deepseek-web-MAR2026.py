import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import numpy as np

def draw_tai_an_floor_plan():
    """
    待庵 (Tai-an) 平面图绘制
    根据典型的茶室布局绘制，尺寸为示意性。
    待庵是千利休设计的著名茶室，位于京都大山崎妙喜庵。
    特点：极小的空间（约2叠台目），躙口（nijiriguchi，小入口），床之间（tokonoma），
    胜手付（kattetsuke，准备区），点前座（temaeza，点茶位）。
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # 背景色（米色，模拟土墙）
    ax.add_patch(Rectangle((0, 0), 10, 8, facecolor='#f5e7d9', edgecolor='none', zorder=0))
    
    # ----- 主室（茶室主体）约2叠台目（示意尺寸：宽3.0m，深2.7m）-----
    # 坐标原点设为左下角 (2, 1) 开始绘制茶室主体
    room_x, room_y = 2.0, 1.0
    room_w, room_h = 3.6, 3.2   # 宽 x 高（深）
    
    # 墙壁 (外侧轮廓)
    wall_color = '#bc9a6c'
    wall_thick = 0.08
    # 外墙填充
    ax.add_patch(Rectangle((room_x, room_y), room_w, room_h, 
                           facecolor='#e7d6bf', edgecolor='#8b5a2b', linewidth=2, zorder=1))
    
    # 绘制内部榻榻米区域 (示意2叠 + 点前座区域)
    # 榻榻米颜色
    tatami_color = '#d9c5a7'
    # 床之间 (tokonoma) 位于左侧或北侧？待庵中床之间位于北侧（图纸上方或左上方），这里设为左侧墙壁处
    toko_x = room_x
    toko_y = room_y + room_h - 1.2
    toko_w = 0.9
    toko_h = 1.2
    ax.add_patch(Rectangle((toko_x, toko_y), toko_w, toko_h, 
                           facecolor='#c8b28b', edgecolor='#6b4c2c', linewidth=1.5, zorder=2))
    ax.text(toko_x + toko_w/2, toko_y + toko_h/2, '床之间\n(Tokonoma)', 
            ha='center', va='center', fontsize=9, color='#4a2a1a', weight='bold')
    
    # 主榻榻米区域 (2叠) 划分为两个榻榻米纹路
    tatami_w = 0.95
    tatami_h = 1.9
    # 第一叠 (点前侧附近)
    tatami1_x = room_x + 1.0
    tatami1_y = room_y + 0.2
    ax.add_patch(Rectangle((tatami1_x, tatami1_y), tatami_w, tatami_h, 
                           facecolor=tatami_color, edgecolor='#9c7a4a', linewidth=1.2, zorder=2))
    # 榻榻米边缘的线 (模拟目积)
    for i in range(1, 3):
        ax.plot([tatami1_x, tatami1_x+tatami_w], [tatami1_y + i*tatami_h/3, tatami1_y + i*tatami_h/3],
                color='#b87c4a', linewidth=0.8, alpha=0.6)
    
    # 第二叠 (客位侧)
    tatami2_x = room_x + 2.0
    tatami2_y = room_y + 0.2
    ax.add_patch(Rectangle((tatami2_x, tatami2_y), tatami_w, tatami_h, 
                           facecolor=tatami_color, edgecolor='#9c7a4a', linewidth=1.2, zorder=2))
    for i in range(1, 3):
        ax.plot([tatami2_x, tatami2_x+tatami_w], [tatami2_y + i*tatami_h/3, tatami2_y + i*tatami_h/3],
                color='#b87c4a', linewidth=0.8, alpha=0.6)
    
    # 点前座 (temaeza) 区域 - 使用半叠大小
    temae_x = room_x + 0.1
    temae_y = room_y + 0.2
    temae_w = 0.85
    temae_h = 1.9
    ax.add_patch(Rectangle((temae_x, temae_y), temae_w, temae_h, 
                           facecolor='#e3cfae', edgecolor='#9c7a4a', linewidth=1, linestyle='--', zorder=2, alpha=0.9))
    ax.text(temae_x + temae_w/2, temae_y + temae_h/2, '点前座\n(Temaeza)', 
            ha='center', va='center', fontsize=8, color='#4a2a1a')
    
    # ----- 躙口 (nijiriguchi) 小型入口 -----
    # 通常位于茶室正面下侧或侧面，这里设在右下角
    niji_x = room_x + room_w - 0.8
    niji_y = room_y
    niji_w = 0.8
    niji_h = 0.7
    # 入口凹陷表示
    ax.add_patch(Rectangle((niji_x, niji_y), niji_w, niji_h, 
                           facecolor='#d2b48c', edgecolor='#6b4c2c', linewidth=2, zorder=3))
    # 画弧形示意小门
    arc = patches.Arc((niji_x + niji_w/2, niji_y + niji_h/2), niji_w*0.7, niji_h*0.6, 
                      angle=0, theta1=0, theta2=180, color='#6b4c2c', linewidth=1.5)
    ax.add_patch(arc)
    ax.text(niji_x + niji_w/2, niji_y + niji_h/3, '躙口\n(Nijiriguchi)', 
            ha='center', va='center', fontsize=7, color='#4a2a1a')
    
    # ----- 胜手付（水屋侧出入口）-----
    katt_x = room_x + room_w
    katt_y = room_y + room_h - 1.2
    katt_w = 0.7
    katt_h = 1.0
    ax.add_patch(Rectangle((katt_x, katt_y), katt_w, katt_h, 
                           facecolor='#c6a87c', edgecolor='#6b4c2c', linewidth=1.5, zorder=2))
    ax.text(katt_x + katt_w/2, katt_y + katt_h/2, '胜手付\n(Kattetsuke)', 
            ha='center', va='center', fontsize=7, color='#4a2a1a', rotation=90)
    
    # ----- 炉 (ro) 位置，通常位于点前座前方 -----
    ro_center_x = temae_x + temae_w/2 + 0.2
    ro_center_y = temae_y + temae_h/3
    ro_radius = 0.35
    ro_circle = Circle((ro_center_x, ro_center_y), ro_radius, 
                       facecolor='#6f4f37', edgecolor='#3e2a1f', linewidth=1.5, zorder=3)
    ax.add_patch(ro_circle)
    ax.text(ro_center_x, ro_center_y, '炉\n(Ro)', ha='center', va='center', fontsize=8, color='white', weight='bold')
    
    # 添付：水指位置示意（点前座附近）
    mizusashi_x = temae_x + 0.2
    mizusashi_y = temae_y + 1.2
    ax.add_patch(Rectangle((mizusashi_x, mizusashi_y), 0.4, 0.4, 
                           facecolor='#b0a07c', edgecolor='#6b4c2c', linewidth=1, zorder=3))
    ax.text(mizusashi_x+0.2, mizusashi_y+0.2, '水指', ha='center', va='center', fontsize=6)
    
    # ----- 窗户示意（茶室常见的连子窗）-----
    # 左侧墙高窗
    window1_x = room_x - 0.15
    window1_y = room_y + 2.0
    window_w, window_h = 0.4, 0.8
    for i in range(3):
        ax.add_patch(Rectangle((window1_x, window1_y + i*0.28), window_w, 0.22, 
                               facecolor='#b9d2e8', edgecolor='#5a3e28', linewidth=0.8, zorder=2))
    # 后方墙窗
    window2_x = room_x + 1.5
    window2_y = room_y + room_h - 0.1
    for i in range(4):
        ax.add_patch(Rectangle((window2_x + i*0.45, window2_y), 0.35, 0.25, 
                               facecolor='#b9d2e8', edgecolor='#5a3e28', linewidth=0.8, zorder=2))
    
    # ----- 标题和注解 -----
    ax.text(5, 7.5, '待庵 (Tai-an) 平面図', fontsize=16, ha='center', weight='bold', color='#4a2a1a')
    ax.text(5, 7.0, '千利休 設計 ・ 妙喜庵 所在', fontsize=10, ha='center', style='italic', color='#6b4c2c')
    
    # 尺度参考线（示意）
    ax.plot([0.5, 2.0], [0.3, 0.3], color='gray', linewidth=1)
    ax.text(1.25, 0.25, '1.5 m (参考)', ha='center', fontsize=7, color='gray')
    
    # 注釈表示区域
    notes = "主室: 約2叠台目\n躙口: 茶道用小型入口\n床之間: 掛軸・花入\n点前座: 亭主動作位置"
    ax.text(8.2, 1.5, notes, fontsize=7, bbox=dict(facecolor='#f0e4d0', edgecolor='#bc9a6c', boxstyle='round,pad=0.3'),
            verticalalignment='top', color='#3a2a1a')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_tai_an_floor_plan()
