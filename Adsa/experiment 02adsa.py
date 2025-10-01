class HashTable:
    def __init__(self, size, strategy):
        self.size = size
        self.table = [None] * size
        self.strategy = strategy
        self.c1 = 1  # for quadratic probing
        self.c2 = 3

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 1 + (key % (self.size - 1))  # non-zero for double hashing

    def get_index(self, key, i):
        if self.strategy == "linear":
            return (self.h1(key) + i) % self.size
        elif self.strategy == "quadratic":
            return (self.h1(key) + self.c1 * i + self.c2 * i * i) % self.size
        elif self.strategy == "double":
            return (self.h1(key) + i * self.h2(key)) % self.size

    def insert(self, key):
        for i in range(self.size):
            index = self.get_index(key, i)
            if self.table[index] is None:
                self.table[index] = key
                print(f"Inserted {key} at index {index}")
                return
            elif self.table[index] == key:
                print(f"{key} already exists at index {index}")
                return
        print(f"Hash table is full! Could not insert {key}")

    def delete(self, key):
        for i in range(self.size):
            index = self.get_index(key, i)
            if self.table[index] == key:
                self.table[index] = None
                print(f"Deleted {key} from index {index}")
                return
            elif self.table[index] is None:
                print(f"{key} not found in the hash table")
                return
        print(f"{key} not found in the hash table")

    def display(self):
        print("\nHash Table:")
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val if val is not None else 'Empty'}")


def main():
    while True:
        size = int(input("\nEnter the size of the hash table: "))
        print("\nChoose collision resolution strategy:")
        print("1. Linear Probing")
        print("2. Quadratic Probing")
        print("3. Double Hashing")
        strategy_choice = int(input("Enter your choice (1/2/3): "))

        strategies = {1: "linear", 2: "quadratic", 3: "double"}
        strategy = strategies.get(strategy_choice, "linear")

        ht = HashTable(size, strategy)

        n = int(input("How many keys do you want to insert? "))
        for _ in range(n):
            key = int(input("Enter key: "))
            ht.insert(key)

        print("\nFinal hash table after insertion:")
        ht.display()


        # Ask if the user wants to continue
        continue_choice = input("\nDo you want to try another hashing method or exit? (1: Another method, 2: Exit): ")
        if continue_choice == "2":
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
