products = [104, 101, 102, 103, 104, 105, 103, 107]

# traverse from right, keep first time seen (which is last in original list)
seen = set()
result_reversed = []

for pid in reversed(products):
    if pid not in seen:
        seen.add(pid)
        result_reversed.append(pid)

# reverse back to original order of last occurrences
last_products = list(reversed(result_reversed))

print("Last product IDs:", last_products)
# Output: Last product IDs: [101, 102, 104, 105, 103, 107]