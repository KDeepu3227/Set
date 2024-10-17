'''
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
Note: There is trailing space at the end of output
'''
n=int(input("enter the elements: "))
values = set()
for _ in range(n):
    values.add(int(input("enter the elements: ")))
print(" ".join(str(val) for val in sorted(values)), end=" ")
'''
enter the elements: 5
enter the elements: 3
enter the elements: 1
enter the elements: 4
enter the elements: 5
enter the elements: 2
1 2 3 4 5 
