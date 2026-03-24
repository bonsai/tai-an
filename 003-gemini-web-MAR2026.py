import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_taian():
    fig, ax = plt.subplots(figsize=(8, 10))
    
    # 単位は mm (京間サイズを基準)
    tatami_w = 955
    tatami_h = 1910
    
    # 全体の設定
    ax.set_xlim(-500, 2500)
    ax.set_ylim(-500, 3500)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- 畳の描画 ---
    # 手前畳 (客畳)
    ax.add_patch(patches.Rectangle((0, 0), tatami_h, tatami_w, fill=True, facecolor='#e5e4d2', edgecolor='black', linewidth=2))
    # 奥畳 (道具畳)
    ax.add_patch(patches.Rectangle((0, tatami_w), tatami_h, tatami_w, fill=True, facecolor='#e5e4d2', edgecolor='black', linewidth=2))

    # --- 床の間 (Tokonoma) ---
    # 北側に配置
    ax.add_patch(patches.Rectangle((0, tatami_w * 2), tatami_h, 900, fill=True, facecolor='#f5f5f5', edgecolor='black', linewidth=2))
    ax.text(tatami_h/2, tatami_w * 2 + 450, '床の間', ha='center', va='center', fontsize=12)

    # --- 次の間 / 控えの間 ---
    # 西側のスペース
    ax.add_patch(patches.Rectangle((-400, 0), 400, tatami_w * 2, fill=False, edgecolor='black', linestyle='--'))
    ax.text(-200, tatami_w, '次の間', rotation=90, ha='center', va='center')

    # --- 入口と出口のラベル ---
    # にじり口 (南側)
    ax.annotate('にじり口', xy=(tatami_h - 600, 0), xytext=(tatami_h - 600, -300),
                arrowprops=dict(arrowstyle='->'))
    
    # 茶道口
    ax.text(-100, tatami_w + 500, '茶道口', rotation=90, va='center')

    # タイトル
    plt.title('待庵 (Taian) 推定平面レイアウト', fontsize=15, pad=20)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_taian()
