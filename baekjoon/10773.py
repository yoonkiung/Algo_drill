from typing import Any
from collections import deque
import sys

class Stack:

    def __init__(self, maxlen: int = 256) -> None:
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return (len(self.__stk))

    def is_empty(self) -> bool:
        return (not self.__stk)

    def is_full(self) -> bool:
        return (len(self.__stk) == self.__stk.maxlen)

    def push(self, value: Any) -> None:
        self.__stk.append(value)
    
    def pop(self) -> None:
        if (self.is_empty() == True):
            return(-1)
        else:
            return(self.__stk.pop())

    def peek(self) -> Any:
        return self.__stk.pop()

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> int:
        print(list(self.__stk))


if __name__ == '__main__':
    
    k = int(sys.stdin.readline())
    stack = Stack(k)

    for i in range(k):
        n = int(sys.stdin.readline())
        
        if (n == 0):
            stack.pop()
        else:
            stack.push(n)
    
    sum = 0
    while (1):
        temp = stack.pop()
        if temp == -1:
            print(sum)
            break
        else:
            sum += temp

        