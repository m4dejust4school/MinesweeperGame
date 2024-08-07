GRID_SIZE = 6
WIDTH = GRID_SIZE * 200
HEIGHT = GRID_SIZE * 120
CELL_COUNT = GRID_SIZE**2
MINES_COUNT = (CELL_COUNT) // 4
LEFT_CLICK_STR = "<Button-1>"
RIGHT_CLICK_STR = "<Button-3>"
# Constants for the UI design
BUTTON_BG_COLOR = "#3C3C3C"
BUTTON_ACTIVE_BG_COLOR = "#474747"
BUTTON_TEXT_COLOR = "#F0F0F0"
BUTTON_BORDER_COLOR = "#5A5A5A"
HIGHLIGHT_COLOR = "#FF6347"
FLAG_COLOR = "#FFD700"
FONT_FAMILY = "Helvetica"
WINDOW_BG_COLOR = "#2C2C2C"

SURROUNDED_COLORS = {
    0: "#2C2C2C",  # Dark Gray
    1: "#3498DB",  # Bright Blue
    2: "#E74C3C",  # Vibrant Red
    3: "#2ECC71",  # Fresh Green
    4: "#F1C40F",  # Warm Yellow
    5: "#9B59B6",  # Soft Purple
    6: "#E67E22",  # Warm Orange
    7: "#1ABC9C",  # Teal
    8: "#E91E63",  # Vibrant Pink
}
