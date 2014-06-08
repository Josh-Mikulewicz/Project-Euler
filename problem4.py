#!/usr/bin/python

import sys


def is_Palindrome(number):
	reverse = str(number)[::-1]
	return str(number) == reverse


def largest(n):
    max_palindrome = 1
    for x in range(n,1,-1):
        for y in range(n,x-1,-1):
            if is_Palindrome(x*y) and x*y > max_palindrome:
                max_palindrome = x*y
            elif x * y < max_palindrome:
                break
    return max_palindrome

  
def main():
    
    print largest(999)

if __name__ == '__main__':
    main()