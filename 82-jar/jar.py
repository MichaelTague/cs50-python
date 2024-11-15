class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, cookies):
        if cookies < 0 or cookies > self._capacity:
            raise ValueError
        self._size = cookies

def main():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(3)
    print(jar)

if __name__ == "__main__":
    main()