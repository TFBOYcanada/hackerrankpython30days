#numScores = int(input())  # not needed for Python
#scores = list(map(int, input().split()))
scores = [1, 2, 3, 4, 5, 4, 3]
scores.sort()
b = len(scores)
if b % 2 == 0:
    median = 0.5 * (scores[(b // 2)] + scores[(b // 2) - 1])
else:
    median = 0.5 * (scores[(b - 1) // 2])
print(sum(scores) // b)
print(median)
highfr = 1
j = 0
mode = []
for item in scores:
    mode.append(scores.count(item))

k = mode.index(max(mode))
print(scores[k])
