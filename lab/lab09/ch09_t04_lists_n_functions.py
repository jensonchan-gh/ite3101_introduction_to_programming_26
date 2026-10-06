# Write your function below!

def fizz_count(x: list[str]):
    count = 0
    for item in x:
        if item == "Fizz" :
            count += 1
    return count


print(fizz_count(["fizz", "cat", "fizz", "fizz"]))