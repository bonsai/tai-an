"""
待庵 (Taian) 平面図
千利休設計・二畳台目の茶室
妙喜庵 (山崎) 所在・国宝
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as pe
import numpy as np

# ──────────────────────────────────────────────
# 設定
# ──────────────────────────────────────────────
plt.rcParams["font.family"] = ["Noto Sans CJK JP", "Hiragino Sans", "Yu Gothic", "sans-serif"]

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect("equal")
ax.axis("off")

# 単位: cm
WALL = 15     # 壁厚
W = 15        # 畳の短辺 (91 cm → ここでは1unit=6cm で 15u ≈ 91cm)
L = 30        # 畳の長辺 (182 cm → 30u)
D = 22        # 台目畳の長辺 (136 cm → 22u)
TW = 15       # 床の間の幅
TD = 12       # 床の間の奥行き

# 色
C_WALL      = "#5C4A32"   # 壁
C_TATAMI    = "#C8B98A"   # 畳
C_TATAMI2   = "#BCA97A"   # 台目畳 (少し濃い)
C_TOKO      = "#D4C9A0"   # 床の間
C_RO        = "#3A2A18"   # 炉
C_FLOOR     = "#E8DFC8"   # 土間・外部
C_NIJI      = "#F5EDD8"   # 躙り口
C_TEXT      = "#2C1A0A"
C_GRID      = "#A08050"   # 畳の目

# ──────────────────────────────────────────────
# 背景
# ──────────────────────────────────────────────
fig.patch.set_facecolor("#F0E8D8")
ax.set_facecolor("#F0E8D8")

# ──────────────────────────────────────────────
# 部屋の外形 (外壁を含む)
# ──────────────────────────────────────────────
#  y
#  ↑
#  +---床の間(TW×TD)---+---台目畳(W×D)---+
#  |                   |                  |
#  +-------------------+                  |
#  |      客  畳 (L×W)                   |
#  |                                      |
#  +------------------------[躙り口]--------+→ x
#
# 室内左下を (0,0) とする

room_x0 = 0
room_y0 = 0
room_w  = L + WALL * 2           # 外壁含む全幅
room_h  = W + D + WALL * 2       # 外壁含む全高

# 外壁塗り (灰茶)
outer = patches.Rectangle(
    (-WALL, -WALL), room_w + WALL*0, room_h + WALL*0,
    linewidth=0, facecolor=C_WALL, zorder=1
)
ax.add_patch(outer)

# 室内床
inner = patches.Rectangle(
    (0, 0), L, W + D,
    linewidth=0, facecolor=C_FLOOR, zorder=2
)
ax.add_patch(inner)

# ──────────────────────────────────────────────
# 客畳 (1枚, L×W)  下段
# ──────────────────────────────────────────────
kaku_x, kaku_y = 0, 0
kaku_w, kaku_h = L, W

kaku = patches.Rectangle(
    (kaku_x, kaku_y), kaku_w, kaku_h,
    linewidth=1.2, edgecolor=C_GRID, facecolor=C_TATAMI, zorder=3
)
ax.add_patch(kaku)

# 畳の目 (横縞)
for yi in np.arange(kaku_y + 1.5, kaku_y + kaku_h, 3):
    ax.plot([kaku_x, kaku_x + kaku_w], [yi, yi],
            color=C_GRID, linewidth=0.4, alpha=0.5, zorder=4)

# ──────────────────────────────────────────────
# 台目畳 (右上, W×D)
# ──────────────────────────────────────────────
daime_x, daime_y = L - W, W
daime_w, daime_h = W, D

daime = patches.Rectangle(
    (daime_x, daime_y), daime_w, daime_h,
    linewidth=1.2, edgecolor=C_GRID, facecolor=C_TATAMI2, zorder=3
)
ax.add_patch(daime)

# 畳の目 (縦縞 → 横畳と直交)
for xi in np.arange(daime_x + 1.5, daime_x + daime_w, 3):
    ax.plot([xi, xi], [daime_y, daime_y + daime_h],
            color=C_GRID, linewidth=0.4, alpha=0.5, zorder=4)

# ──────────────────────────────────────────────
# 床の間 (左上, TW×TD)  ← 実際は壁面に接する
# ──────────────────────────────────────────────
toko_x, toko_y = 0, W + (D - TD)
toko_w, toko_h = TW, TD

toko_bg = patches.Rectangle(
    (toko_x, toko_y), toko_w, toko_h,
    linewidth=2, edgecolor=C_WALL, facecolor=C_TOKO, zorder=3
)
ax.add_patch(toko_bg)

# 床框 (框線)
ax.plot([toko_x, toko_x + toko_w], [toko_y, toko_y],
        color=C_WALL, linewidth=3, zorder=5)

# 床の間テクスチャ (木目風ハッチ)
for xi in np.arange(toko_x + 1, toko_x + toko_w, 2):
    ax.plot([xi, xi], [toko_y, toko_y + toko_h],
            color="#B8A070", linewidth=0.3, alpha=0.6, zorder=4)

# ──────────────────────────────────────────────
# 炉 (台目切り) 台目畳の左下隅
# ──────────────────────────────────────────────
ro_size = 4.5
ro_x = daime_x + 1.5
ro_y = daime_y + 1.5

ro = patches.Rectangle(
    (ro_x, ro_y), ro_size, ro_size,
    linewidth=1.5, edgecolor="#8B7050", facecolor=C_RO, zorder=5
)
ax.add_patch(ro)

# 炉縁 (框)
ro_edge = patches.Rectangle(
    (ro_x - 0.5, ro_y - 0.5), ro_size + 1, ro_size + 1,
    linewidth=1.5, edgecolor="#7A5A30", facecolor="none", zorder=5
)
ax.add_patch(ro_edge)

# 炉の灰 (十字の光)
cx = ro_x + ro_size / 2
cy = ro_y + ro_size / 2
for angle in [0, 90, 45, 135]:
    rad = np.radians(angle)
    ax.plot([cx - np.cos(rad)*1.5, cx + np.cos(rad)*1.5],
            [cy - np.sin(rad)*1.5, cy + np.sin(rad)*1.5],
            color="#6A4020", linewidth=0.6, alpha=0.7, zorder=6)

# ──────────────────────────────────────────────
# 躙り口 (右下壁に開口)
# ──────────────────────────────────────────────
niji_w = 5    # 開口幅
niji_h = WALL
niji_x = L - niji_w - 3
niji_y = -WALL

niji = patches.Rectangle(
    (niji_x, niji_y), niji_w, niji_h,
    linewidth=0, facecolor=C_NIJI, zorder=3
)
ax.add_patch(niji)

# 躙り口の枠
ax.plot([niji_x, niji_x], [-WALL, 0], color=C_WALL, linewidth=2.5, zorder=6)
ax.plot([niji_x + niji_w, niji_x + niji_w], [-WALL, 0], color=C_WALL, linewidth=2.5, zorder=6)

# ──────────────────────────────────────────────
# 壁の仕上げ線 (内壁ライン)
# ──────────────────────────────────────────────
# 外周
for xy, ww, hh in [
    ((0, 0), L, W+D),  # 内壁矩形
]:
    rect = patches.Rectangle(
        xy, ww, hh,
        linewidth=2.5, edgecolor=C_WALL, facecolor="none", zorder=7
    )
    ax.add_patch(rect)

# 床の間の仕切り壁 (客畳と台目畳の境)
ax.plot([toko_x + toko_w, daime_x], [W + D - TD, W + D - TD],
        color=C_WALL, linewidth=2.5, zorder=7)
ax.plot([toko_x + toko_w, toko_x + toko_w], [W, W + D],
        color=C_WALL, linewidth=2.5, zorder=7)

# 客畳と台目畳の境界線
ax.plot([daime_x, daime_x], [W, W + D],
        color=C_GRID, linewidth=1.5, linestyle="--", alpha=0.6, zorder=6)

# 下客畳と上ゾーンの境界
ax.plot([0, L], [W, W],
        color=C_GRID, linewidth=1.2, zorder=6)

# ──────────────────────────────────────────────
# 方位記号
# ──────────────────────────────────────────────
compass_x, compass_y = L + 6, W + D - 8
r = 4
circle = plt.Circle((compass_x, compass_y), r,
                     fill=False, edgecolor=C_TEXT, linewidth=1.2, zorder=10)
ax.add_patch(circle)
# 北矢印
ax.annotate("", xy=(compass_x, compass_y + r + 0.5),
            xytext=(compass_x, compass_y),
            arrowprops=dict(arrowstyle="-|>", color=C_TEXT, lw=1.5), zorder=10)
ax.text(compass_x, compass_y + r + 1.5, "北", ha="center", va="bottom",
        fontsize=8, color=C_TEXT, fontweight="bold")

# ──────────────────────────────────────────────
# ラベル
# ──────────────────────────────────────────────
label_kw = dict(ha="center", va="center", fontsize=9, color=C_TEXT,
                fontweight="bold", zorder=9)
note_kw  = dict(ha="center", va="center", fontsize=7, color="#5A4020",
                style="italic", zorder=9)

# 客畳
ax.text(kaku_x + kaku_w/2, kaku_y + kaku_h/2 + 1,
        "客　畳", **label_kw)
ax.text(kaku_x + kaku_w/2, kaku_y + kaku_h/2 - 2,
        "(一畳)", **note_kw)

# 台目畳
ax.text(daime_x + daime_w/2, daime_y + daime_h/2 + 2,
        "台目畳", **label_kw)
ax.text(daime_x + daime_w/2, daime_y + daime_h/2,
        "(点前座)", **note_kw)

# 床の間
ax.text(toko_x + toko_w/2, toko_y + toko_h/2,
        "床の間", ha="center", va="center",
        fontsize=8, color=C_TEXT, fontweight="bold",
        rotation=0, zorder=9)

# 炉
ax.text(ro_x + ro_size/2, ro_y - 1.8,
        "炉", ha="center", va="top",
        fontsize=8, color="#F0D090", fontweight="bold", zorder=9)

# 躙り口
ax.text(niji_x + niji_w/2, -WALL - 2,
        "躙り口", ha="center", va="top",
        fontsize=8, color=C_TEXT, fontweight="bold", zorder=9)

# ──────────────────────────────────────────────
# 寸法線 (簡易)
# ──────────────────────────────────────────────
def dim_line(ax, x1, y1, x2, y2, label, side="center"):
    mx, my = (x1+x2)/2, (y1+y2)/2
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="<->", color="#7A6040", lw=1.0))
    offset = 1.5
    ax.text(mx, my + offset, label, ha="center", va="bottom",
            fontsize=6.5, color="#7A6040")

# 幅方向 (下)
dim_y = -WALL - 7
ax.annotate("", xy=(L, dim_y), xytext=(0, dim_y),
            arrowprops=dict(arrowstyle="<->", color="#7A6040", lw=1.0), zorder=8)
ax.plot([0, 0], [-WALL - 4, dim_y], color="#7A6040", lw=0.7, ls="--", zorder=8)
ax.plot([L, L], [-WALL - 4, dim_y], color="#7A6040", lw=0.7, ls="--", zorder=8)
ax.text(L/2, dim_y - 1.5, "約 2,730 mm", ha="center", va="top",
        fontsize=7, color="#7A6040")

# 高さ方向 (右)
dim_x = L + 2
ax.annotate("", xy=(dim_x, W+D), xytext=(dim_x, 0),
            arrowprops=dict(arrowstyle="<->", color="#7A6040", lw=1.0), zorder=8)
ax.text(dim_x + 1, (W+D)/2, "約 2,730 mm",
        ha="left", va="center", fontsize=7, color="#7A6040", rotation=90)

# ──────────────────────────────────────────────
# タイトル・凡例
# ──────────────────────────────────────────────
ax.text(L/2, W + D + WALL + 1,
        "待 庵  平 面 図",
        ha="center", va="bottom", fontsize=16,
        color=C_TEXT, fontweight="bold",
        fontfamily=["Noto Serif CJK JP", "Hiragino Mincho ProN", "serif"])

ax.text(L/2, W + D + WALL + 4.5,
        "千利休設計 ／ 二畳台目 ／ 妙喜庵（山崎）国宝",
        ha="center", va="bottom", fontsize=8,
        color="#7A6040")

# 凡例
legend_x, legend_y = -WALL, W + 3
items = [
    (C_TATAMI,  "客畳"),
    (C_TATAMI2, "台目畳（点前座）"),
    (C_TOKO,    "床の間"),
    (C_RO,      "炉"),
]
for i, (color, label) in enumerate(items):
    bx = legend_x
    by = legend_y - i * 4
    rect = patches.Rectangle((bx, by), 3, 2.5,
                               facecolor=color, edgecolor=C_WALL, linewidth=0.8)
    ax.add_patch(rect)
    ax.text(bx + 4, by + 1.2, label, va="center", fontsize=7, color=C_TEXT)

# スケールバー
sb_x, sb_y = -WALL, -WALL - 5
sb_len = 9.1  # 91cm = 1尺相当
ax.plot([sb_x, sb_x + sb_len], [sb_y, sb_y], color=C_TEXT, lw=2, zorder=9)
ax.plot([sb_x, sb_x], [sb_y - 0.5, sb_y + 0.5], color=C_TEXT, lw=2, zorder=9)
ax.plot([sb_x + sb_len, sb_x + sb_len], [sb_y - 0.5, sb_y + 0.5], color=C_TEXT, lw=2, zorder=9)
ax.text(sb_x + sb_len/2, sb_y - 1.5, "910 mm (1 間)", ha="center", va="top",
        fontsize=6.5, color=C_TEXT)

# ──────────────────────────────────────────────
# 軸設定
# ──────────────────────────────────────────────
margin = 18
ax.set_xlim(-WALL - margin, L + margin + 12)
ax.set_ylim(-WALL - margin, W + D + WALL + margin)

plt.tight_layout(pad=0)
plt.savefig("/mnt/user-data/outputs/taian_floor_plan.png",
            dpi=180, bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("saved.")
plt.show()
