class DigitOperations:
    def calculate_pairs_sum(self, num):
        digits = [int(d) for d in str(num)]
        total = 0
        
        # Sum of all pairs (i < j)
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                total += digits[i] + digits[j]
        
        return total


class SumCalculator(DigitOperations):
    def get_sum(self, num):
        return self.calculate_pairs_sum(num)


# Main()
n = int(input())
obj = SumCalculator()
print(obj.get_sum(n))