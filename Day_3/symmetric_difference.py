_ = int(input())
SET_N = set(map(int, input().split()))
_ = int(input())
SET_B = set(map(int, input().split()))
print(len(SET_N.symmetric_difference(SET_B)))

#as it is a hackerrank problem you can change the sets
