a = int(input())
answer = ""

for i in range(a):
	word1 = set(input())
	word2 = set(input())
	res = word1.intersection(word2)
	if len(res) > 0:
		answer = answer + "YES "
	else:
		answer = answer + "NO "

for i in answer.split():
	print(i)