class PairFinder:
    def _init_(self, target, arr):
        self.target = target
        self.arr = arr

    def find_pairs(self):
        result = []
        n = len(self.arr)

        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i] + self.arr[j] == self.target:
                    result.append((self.arr[i], self.arr[j]))

        return result


# ---- Main Program ----
target = int(input())
n = int(input())
arr = list(map(int, input().split()))

obj = PairFinder(target, arr)
pairs = obj.find_pairs()

for a, b in pairs:
    print(f"{a} + {b} = {target}")