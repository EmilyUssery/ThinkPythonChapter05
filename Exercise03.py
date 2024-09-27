#!/usr/bin/env python3

def is_triangle_naive(s1, s2, s3):
    if s1 > s2 + s3:
        print("No")
    elif s2 > s1 + s3:
        print("No")
    elif s3 > s1 + s2:
        print("No")
    else:
        print("Yes")

def is_triangle(s1, s2, s3):
    print("No") if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2 else print("Yes")

is_triangle_naive(4, 5, 6)
is_triangle_naive(1, 2, 3)
is_triangle_naive(6, 2, 3)
is_triangle_naive(1, 1, 12)
is_triangle_naive(3, 4, 5)
print("-"*80)
is_triangle(4, 5, 6)
is_triangle(1, 2, 3)
is_triangle(6, 2, 3)
is_triangle(1, 1, 12)
is_triangle(3, 4, 5)