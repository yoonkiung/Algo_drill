def factorial(n :int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1
    
# if __name__ == '__main__':
#     n = int(input())
#     print(f'{factorial(n)}')

def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     print(f'{gcd(x, y)}')

def recur(n: int) -> None:
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)

    #상향식 분석과 하향식 분석

# if __name__ == '__main__':
#     n = recur(int(input()))

def recur_remove_tail(n: int) -> None:
    while n > 0:
        recur_remove_tail(n - 1)
        print(n)
        n = n - 2

# if __name__ == '__main__':
#     n = recur_remove_tail(int(input()))

from stack_deque import Stack

def recur_iter(n: int) -> None:
    s = Stack(n)
    while (True):
        if n > 0:
            s.push(n)
            n -= 1
            continue
        if not s.is_empty():
            n = s.pop()
            print(n)
            n -= 2
            continue
        break

if __name__ == '__main__':
    n = recur_iter(int(input()))
