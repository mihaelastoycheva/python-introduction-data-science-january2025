words = input().split()
searched_palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
print(found_palindromes)

palindrome_repetitions = found_palindromes.count(searched_palindrome)

print(f"Found palindrome {palindrome_repetitions} times")
