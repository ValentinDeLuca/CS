"""Make the Sieve of Eratosthenes: a function that calculates prime numbers, also
known in Ancient Greece. Choose an integer n : this function will calculate all prime
numbers up to n . First, create a set and enter all the integers from 2 to n then
eliminate from the set all multiples of 2, except 2 (ie 4, 6, 8, 10, 12, ...), then
eliminate all multiples of 3, except 3 (ie 6, 9, 12, 15, ...) and continue like𝑛𝑛 this,
erasing each time the multiples of the minimum value present in the set, up to the
number . The numbers left in the set are those required√𝑛𝑛"""
def main():
    n = int(input("Choose an integer n: "))
    numbers = set(range(2, n+1))
    print(f"Primes up to {n}: {prime(numbers, 2, n)}")


def prime(numbers, i, n):
    if i <= n:
        numbers = numbers.difference(set(range(i * 2, n + 1, i)))
        return prime(numbers, i + 1, n)
    return sorted(numbers)


if __name__ == '__main__':
    main()
