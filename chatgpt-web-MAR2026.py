import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 部屋サイズ（約2畳：ざっくり2m x 2m）
room_size = 2.0

# 外枠
ax.plot([0, room_size, room_size, 0, 0],
        [0, 0, room_size, room_size, 0])

# にじり口（小さい入口）
ax.plot([0, 0.3], [0.5, 0.5], linewidth=3)

# 炉（中央やや手前）
ax.add_patch(plt.Rectangle((0.8, 0.6), 0.4, 0.4, fill=False))

# 床の間（上側）
ax.add_patch(plt.Rectangle((0.7, 1.5), 0.6, 0.3, fill=False))

# 表示設定
ax.set_aspect('equal')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.set_title("待庵 平面図（簡易）")

plt.grid()
plt.show()
