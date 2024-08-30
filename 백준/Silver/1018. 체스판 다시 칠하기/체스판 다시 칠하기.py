n, m = list(map(int, input().split()))
chess_board = []
for _ in range(n):
    chess_board.append(list(input()))

min_count = 9999

for i in range(n-7):
    for j in range(m-7):
        black_count = 0
        white_count = 0
        for k in range(8):
            for l in range(8):
                if (k + l) % 2 == 0:
                    if chess_board[i+k][j+l] != 'B':
                        black_count += 1
                    if chess_board[i+k][j+l] != 'W':
                        white_count += 1
                else:
                    if chess_board[i+k][j+l] != 'W':
                        black_count += 1
                    if chess_board[i+k][j+l] != 'B':
                        white_count += 1
        min_count = min(min_count, black_count, white_count)

print(min_count)
