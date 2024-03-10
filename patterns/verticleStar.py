for i in range(int(input(""))*2): print(" " * (([0, 2, 4, 2][(i//2) % 4]) * 2)) if i % 2 != 0 else print(" " * (([0, 2, 4, 2][(i//2) % 4]) * 2), end="*\n")
