import math

maxn = 10**5 + 10

vis = [0] * maxn
prime = []
sum = [0] * 1010
k = 0

def init():
    global k
    for i in range(2, maxn):
        if vis[i] == 1:
            continue
        for j in range(2 * i, maxn, i):
            vis[j] = 1
        vis[i] = 1
        prime.append(i)
        k += 1

def main():
    init()
    t = int(input())
    for _ in range(t):
        sum = [0] * 1010
        n, name = input().split()
        n = int(n)
        m = n
        tot = 0
        for i in range(k):
            if prime[i] * prime[i] > m:
                break
            if m % prime[i] == 0:
                while m % prime[i] == 0:
                    sum[tot] += 1
                    m //= prime[i]
                tot += 1
        if m != 1:
            sum[tot] += 1
            tot += 1
        if tot >= 3:
            print("tie")
        elif tot == 2:
            temp = abs(sum[0] - sum[1])
            if temp == 0:
                print("Bob" if name[0] == 'A' else "Alice")
            elif temp == 1:
                print("Bob" if name[0] == 'B' else "Alice")
            else:
                print("tie")
        elif tot == 1:
            if sum[0] % 2 == 1:
                print("Bob" if name[0] == 'B' else "Alice")
            else:
                print("Bob" if name[0] == 'A' else "Alice")

if __name__ == "__main__":
    main()
