def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False

    return True


number = int(input())

if is_prime(number):
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")
