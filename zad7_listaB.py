# Napisz program rysujący histogram (w konsoli) dla podanej listy liczb
# całkowitych

def solution(x :list[int]) -> None:
    if type(x) != list:
        print(ValueError("Podaj tablice int!"))
    else:
        print("="*(len(x)*2))
        for i in range(max(x), 0, -1):
            line = ""
            for element in x:
                if element >= i:
                    line += "* "
                else:
                    line += "  "
            print(line)
        print("="*(len(x)*2))
        print(*x, sep=" ")


x = [1,9,2,1,5,9,10]
solution(x)