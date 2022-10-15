from math import sqrt
 
def primeCount(arr, n):
     
    # Find maximum value in the array
    max_val = arr[0];
    for i in range(len(arr)):
        if(arr[i] > max_val):
            max_val = arr[i]

    prime =[ True for i in range(max_val + 1)]
 
    # Remaining part of SIEVE
    prime[0] = False
    prime[1] = False
    k = int(sqrt(max_val)) + 1
    for p in range(2, k, 1):
     
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, max_val + 1, p):
                prime[i] = False
 
    # Find all primes in arr[]
    count = 0
    for i in range(0, n, 1):
        if (prime[arr[i]]):
            count += 1
 
    return count
 
# Driver code
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    
 
    print(primeCount(arr, n))
 