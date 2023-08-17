"""
Q1
Rearrange an array of integers so that the calculated value U is maximized. Among the
arrangements that satisfy that test, choose the array with minimal ordering. The value of U
for an array with n elements is calculated as :
U = arr[1]*arr[2]*(1÷arr[3])*arr[4]*...*arr[n-1] * (1÷arr[n]) if n is odd
or
U = arr[1]*arr[2]*(1÷arr[3])*arr[4]*...*(1÷arr[n-1]) * arr[n] if n is even
The sequence of operations is the same in either case, but the length of the array, n,
determines whether the calculation ends on arr[n] or (1÷arr[n]).
Arrange the elements to maximize U and the items are in the numerically smallest possible
order.
"""


def maximize_u(arr):
    n = len(arr)
    arr.sort(reverse=True)

    if n % 2 == 1:
        u = arr[0] * arr[1]
        for i in range(2, n, 2):
            u *= (1 / arr[i]) * arr[i + 1]
    else:
        u = arr[0] * arr[1]
        for i in range(2, n - 1, 2):
            u *= (1 / arr[i]) * arr[i + 1]
        u *= arr[n - 1]

    return u
