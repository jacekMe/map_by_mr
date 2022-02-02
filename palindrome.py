"""sprawdzamy czy liczba całkowita podana na wejściu jest palindromem. Nie konwertujemy liczby całkowitej na łańcuch
np. 121 to palidrom, tak samo jak 777, natomiast 123 nie jest palindromem"""


class Palindrome:
    def __init__(self, arr=None):
        self.arr = arr or []

    def append(self, val=None):
        self.arr.append(val)

    def front(self):
        if not self.isEmpty():
            return self.arr.pop(0)
        else:
            return None

    def back(self):
        if not self.isEmpty():
            return self.arr.pop()
        else:
            return None

    def isEmpty(self):
        return len(self.arr) == 0


def isPalindrome(number):
    palindrome = Palindrome()
    count = 0

    while number > 0:
        digit = number % 10
        number //= 10
        palindrome.append(digit)
        count += 1

    for _ in range(count // 2):
        if palindrome.front() != palindrome.back():
            return False

    return True


def main():
    print(isPalindrome(1234))
    print(isPalindrome(0))
    print(isPalindrome(121))
    print(isPalindrome(777))
    print(isPalindrome(123))
    print(isPalindrome(57654674))


if __name__ == "__main__":
    main()
