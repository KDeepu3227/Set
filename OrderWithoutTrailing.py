'''
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
Note: There is no trailing space at the end of output.
'''
values = set(map(int, input().split()))
print(" ".join(map(str, sorted(values))))
'''
5 3 2 1 7 5
1 2 3 5 7
