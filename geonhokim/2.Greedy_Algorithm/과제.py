class Solution:
    # 오답, 이풀이의 반례
    # 3, (2, 10), (2, 20), (2, 10), (3, 40), (4, 50), (4 70), (4, 100)
    # 이렇게 하면 2일 안에 2개를 해결하고 3, 4일에 2과제를 수행하게 된다.
    # 그러나, 2일까지 과제를 포기하고 3, 4일 과제 4개를 풀어야 한다.
    # 이런식으로 풀면 안된다
    def myself_wrong_answer(self, n: int):
        day_score = {i:[] for i in range(1, 1002)}
        maxDeadline = 0

        for _ in range(n):
            day, score = map(int, input().split())

            day_score[day].append(score)

            maxDeadline = max(maxDeadline, day)
        
        maxScore = 0
        scores = []
        startDay = 1
        for day in range(1, maxDeadline + 2):

            scores = scores + day_score[day]
            # print(f"{day}일, 리스트{scores}")

            if len(scores) > day - startDay + 1:
                # print(f"해당날짜{day}")
                scores.sort(reverse=True)
                # print(scores)
                maxScore += sum(scores[0:day - startDay + 1])

                startDay = day + 1
                scores = []
                
            elif day == maxDeadline + 1:
                maxScore += sum(scores)
                
        return maxScore

    # 그리디 알고리즘답게
    def greedy(self, n: int):
        days = [0 for _ in range(1001)]
        days[0] = 1
        day_score = []

        for _ in range(n):
            day, score = map(int, input().split())
            day_score.append((day, score))
        
        day_score.sort(reverse = True, key = lambda x : (x[1], x[0]))

        for day, score in day_score:
            
            while day > 0 and days[day]:
                day -= 1
            
            if day == 0:
                continue

            days[day] = score

        return sum(days) - 1


sol = Solution()

n = int(input())

print(sol.greedy(n))