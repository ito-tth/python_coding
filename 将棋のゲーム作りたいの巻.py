def create_shogi_board():
    board = [["" for _ in range(9)] for _ in range(9)]

    # 駒の日本語表記
    pieces = {
        "歩": "歩", "香": "香", "桂": "桂", "銀": "銀",
        "金": "金", "角": "角", "飛": "飛", "王": "王"
    }

    # 先手（上側）
    board[0] = [pieces[p] for p in ["香", "桂", "銀", "金", "王", "金", "銀", "桂", "香"]]
    board[1][1] = pieces["飛"]
    board[1][7] = pieces["角"]
    board[2] = [pieces["歩"] for _ in range(9)]

    # 後手（下側）
    board[6] = [pieces["歩"] for _ in range(9)]
    board[7][1] = pieces["角"]
    board[7][7] = pieces["飛"]
    board[8] = [pieces[p] for p in ["香", "桂", "銀", "金", "王", "金", "銀", "桂", "香"]]

    return board

def print_board(board):
    # 列番号
    print("   " + " ".join(str(i+1) for i in range(9)))
    print("  +" + "---+" * 9)
    for i, row in enumerate(board):
        row_str = f"{i+1}|" + "|".join(cell if cell else "  " for cell in row) + "|"
        print(row_str)
        print("  +" + "---+" * 9)

# 実行
if __name__ == "__main__":
    board = create_shogi_board()
    print_board(board)

