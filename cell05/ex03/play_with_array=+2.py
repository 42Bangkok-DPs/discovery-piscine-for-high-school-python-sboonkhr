#!/usr/bin/env python3
import random

def generate_array(size):
    return [random.randint(-20, 50) for _ in range(size)]

def print_array(arr):
    print(arr)

def unique_elements(arr):
    seen = set()
    unique = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)
    return unique

def main():
    original_array = generate_array(10)
    print_array(original_array)
    unique_array = unique_elements(original_array)
    print(f"{set(unique_array)}$")

if __name__ == "__main__":
    main()
