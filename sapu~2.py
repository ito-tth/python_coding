with open('test.txt') as f:
    for i in range(4):
        s_line = f.readline()
        print(s_line)
        if s_line == "" :
            print("終了です")