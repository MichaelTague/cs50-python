class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError
        self.cookies -= n

    @property
    def capacity(self):
        return self.capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies

    @cookies.setter
    def cookies(self, cookies):



def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()