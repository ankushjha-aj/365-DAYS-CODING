N1 = int(input())
storage1 = set(input().split())
N2 = int(input())
storage2 = set(input().split())
storage3 = storage1.difference(storage2)
print(len(storage3))


# As its is a hackerrank problem 

#split divides the string in list with words of a sentence
