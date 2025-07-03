from fibonacci import fibonacci

# Test: pobieramy pierwsze 10 liczb ciągu Fibonacciego
gen = fibonacci()
for _ in range(10):
    print(next(gen))