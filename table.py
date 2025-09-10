num = int(input("Enter a number to create multiplication table: "))
print("================")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print("================")