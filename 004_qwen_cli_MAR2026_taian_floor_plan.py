"""
待庵 (Taian) Tea Room Floor Plan
Sen no Rikyu's famous 2-mat tea room
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

def draw_taian_floor_plan():
    """
    Draw the floor plan of Taian (待庵)
    A traditional 2-mat tea room designed by Sen no Rikyu
    """
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    
    # Room dimensions (in shaku, 1 shaku ≈ 30.3 cm)
    # Taian is approximately 2 tatami mats
    room_width = 4  # shaku
    room_height = 4  # shaku
    
    # Draw main room outline
    room = Rectangle((0, 0), room_width, room_height, 
                     linewidth=3, edgecolor='#8B4513', facecolor='#F5DEB3', 
                     label='Tea Room')
    ax.add_patch(room)
    
    # Draw tatami mat divisions (2 mats)
    # Mat 1 (host side - temaeza)
    mat1 = Rectangle((0, 2), 4, 2, 
                     linewidth=1, edgecolor='#654321', facecolor='#DEB887',
                     alpha=0.5, label='Temaeza (Host)')
    ax.add_patch(mat1)
    
    # Mat 2 (guest side - kyakuza)
    mat2 = Rectangle((0, 0), 4, 2, 
                     linewidth=1, edgecolor='#654321', facecolor='#D2B48C',
                     alpha=0.5, label='Kyakuza (Guest)')
    ax.add_patch(mat2)
    
    # Tokonoma (alcove) - typically on the left side
    tokonoma_x, tokonoma_y = 0, 2.5
    tokonoma_w, tokonoma_h = 1.2, 1.5
    tokonoma = Rectangle((tokonoma_x, tokonoma_y), tokonoma_w, tokonoma_h,
                         linewidth=2, edgecolor='#5C4033', facecolor='#FFE4C4',
                         label='Tokonoma (Alcove)')
    ax.add_patch(tokonoma)
    
    # Tokonoma steps (dan)
    ax.plot([tokonoma_x, tokonoma_x + tokonoma_w], [tokonoma_y + 0.5, tokonoma_y + 0.5],
            color='#5C4033', linewidth=1, linestyle='--')
    
    # Chigaidana (shelves) - staggered shelves next to tokonoma
    shelf1_x, shelf1_y = 1.3, 2.8
    shelf1 = Rectangle((shelf1_x, shelf1_y), 0.8, 0.6,
                       linewidth=2, edgecolor='#5C4033', facecolor='#DEB887')
    ax.add_patch(shelf1)
    
    shelf2_x, shelf2_y = 1.3, 2.2
    shelf2 = Rectangle((shelf2_x, shelf2_y), 0.8, 0.5,
                       linewidth=2, edgecolor='#5C4033', facecolor='#DEB887')
    ax.add_patch(shelf2)
    
    # Mizuya (water preparation area) - small space
    mizuya_x, mizuya_y = 3.2, 2.5
    mizuya_w, mizuya_h = 0.8, 1.0
    mizuya = Rectangle((mizuya_x, mizuya_y), mizuya_w, mizuya_h,
                       linewidth=2, edgecolor='#5C4033', facecolor='#E6E6FA',
                       label='Mizuya (Prep Area)')
    ax.add_patch(mizuya)
    
    # Hearth location (ro) - typically in center of host mat
    ro_center = (2, 3)
    ro = Circle(ro_center, 0.4, linewidth=2, edgecolor='#8B0000', 
                facecolor='#FFD700', label='Ro (Hearth)')
    ax.add_patch(ro)
    
    # Guest entrance (nijiriguchi - crawling entrance)
    entrance_x, entrance_y = 2, 0
    entrance_width = 0.6
    ax.plot([entrance_x - entrance_width/2, entrance_x + entrance_width/2], 
            [entrance_y, entrance_y], 
            color='#8B4513', linewidth=3, linestyle=':')
    ax.text(entrance_x, entrance_y - 0.3, 'Nijiriguchi\n(Guest Entrance)', 
            ha='center', fontsize=9, fontweight='bold')
    
    # Host entrance (sadoriguchi)
    host_entrance_x, host_entrance_y = 3.5, 3.5
    host_entrance_width = 0.5
    ax.plot([host_entrance_x, host_entrance_x], 
            [host_entrance_y - host_entrance_width/2, host_entrance_y + host_entrance_width/2], 
            color='#8B4513', linewidth=2, linestyle='--')
    ax.text(host_entrance_x + 0.4, host_entrance_y, 'Sadoriguchi\n(Host)', 
            ha='left', fontsize=8)
    
    # Hanging scroll position in tokonoma
    ax.text(tokonoma_x + tokonoma_w/2, tokonoma_y + tokonoma_h/2, 
            'Kakejiku\n(Scroll)', ha='center', fontsize=8, 
            color='#5C4033', fontweight='bold')
    
    # Flower vase position
    ax.text(tokonoma_x + tokonoma_w/2, tokonoma_y + 0.3, 
            'Chashitsu\n(Flowers)', ha='center', fontsize=7, color='#5C4033')
    
    # Add dimensions
    ax.text(room_width/2, room_height + 0.3, '4 shaku (≈121 cm)', 
            ha='center', fontsize=10, fontweight='bold')
    ax.text(room_width + 0.3, room_height/2, '4 shaku (≈121 cm)', 
            va='center', fontsize=10, fontweight='bold', rotation=90)
    
    # Add title
    ax.set_title('待庵 (Taian) - Tea Room Floor Plan\nDesigned by Sen no Rikyu (2-mat room)',
                 fontsize=14, fontweight='bold', pad=20)
    
    # Set axis limits with padding
    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.8, 4.8)
    
    # Remove axis ticks
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Set aspect ratio
    ax.set_aspect('equal')
    
    # Add legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.0, -0.1), fontsize=9)
    
    # Add grid for reference
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    
    # Add scale bar
    scale_x, scale_y = 0.2, -0.6
    ax.plot([scale_x, scale_x + 1], [scale_y, scale_y], 
            color='black', linewidth=2, solid_capstyle='round')
    ax.text(scale_x + 0.5, scale_y - 0.15, '1 shaku (≈30.3 cm)', 
            ha='center', fontsize=9)
    
    # Add notes
    notes = """
    Notes:
    • Taian is one of the most famous tea rooms in Japan
    • Located at Myokian-ji Temple in Yamazaki, Kyoto
    • Designed by Sen no Rikyu in the 16th century
    • Represents the wabi-cha aesthetic of simplicity
    • The 2-mat size creates intimate tea ceremonies
    """
    fig.text(0.5, -0.15, notes, ha='center', fontsize=8, 
             bbox=dict(boxstyle='round', facecolor='#FFF8DC', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('taian_floor_plan.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print("Taian floor plan has been generated!")
    print("Output: taian_floor_plan.png")

if __name__ == '__main__':
    draw_taian_floor_plan()
