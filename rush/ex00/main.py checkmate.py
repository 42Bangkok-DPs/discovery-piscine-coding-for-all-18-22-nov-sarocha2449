def is_king_in_check(board_str):
    board = board_str.strip().split('\n')
    size = len(board)

    # ค้นหาตำแหน่งของ King
    king_pos = None
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    if not king_pos:
        print("Error: No King on the board")
        return

    # Helper ฟังก์ชันเพื่อตรวจสอบทิศทาง
    def can_capture_from_direction(x, y, dx, dy, valid_pieces):
        while 0 <= x < size and 0 <= y < size:
            x, y = x + dx, y + dy
            if 0 <= x < size and 0 <= y < size:
                if board[x][y] == '.':
                    continue
                elif board[x][y] in valid_pieces:
                    return True
                else:
                    break
        return False

    # ตรวจสอบทิศทางของ Rook และ Queen (แนวนอนและแนวตั้ง)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if can_capture_from_direction(king_pos[0], king_pos[1], dx, dy, {'R', 'Q'}):
            print("Success")
            return

    # ตรวจสอบทิศทางของ Bishop และ Queen (แนวทแยง)
    for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if can_capture_from_direction(king_pos[0], king_pos[1], dx, dy, {'B', 'Q'}):
            print("Success")
            return

    # ตรวจสอบการเดินของ Pawn (เฉพาะช่องที่ Pawn จับได้)
    pawn_moves = [(-1, -1), (-1, 1)]  # Pawn จับได้เฉพาะด้านบนซ้ายและขวา
    for dx, dy in pawn_moves:
        x, y = king_pos[0] + dx, king_pos[1] + dy
        if 0 <= x < size and 0 <= y < size and board[x][y] == 'P':
            print("Success")
            return

    print("Fail")

# ตารางบอร์ด
board = """
. . . . . . .
. . . Q . . .
. . . . . . .
. K . . . . .
. . . . . . .
"""

# Main
if __name__ == "__main__":
    is_king_in_check(board)