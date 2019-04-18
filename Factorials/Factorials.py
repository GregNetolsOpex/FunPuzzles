def factorial(a, b):
    if a > b:
        return a * factorial(a-b, b)
    else:
        return a

def binary_search(low, high, b, target, function):

    y_low = function(low, b)
    mid = (high+low)/2
    y_mid = function(mid, b)
    y_high = function(high, b)

    if abs(y_mid - target) < (10**-12):
        return mid
    elif y_low < target < y_mid:
        return binary_search(low, mid, b, target, function)
    elif y_mid < target < y_high:
        return binary_search(mid, high, b, target, function)

if __name__ == '__main__':

    new_a = binary_search(2, 20, (3/4), 25, factorial)
    print(new_a)
    print(factorial(new_a,(3/4)))

    print(factorial(5.130178475349293, 3/4))
