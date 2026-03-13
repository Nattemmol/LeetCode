class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        queue = deque()

        for i in bills:
            if i == 5:
                queue.appendleft(i)
            elif i == 10:
                if queue and queue[0] == 5:
                    queue.popleft()
                    queue.append(i)
                else:
                    return False
            elif i == 20:
                if  queue and queue[-1] == 10 and queue[0] == 5:
                    queue.popleft()
                    queue.pop()
                else:
                    for i in range(3):
                        if queue and queue[0] == 5:
                            queue.popleft()
                        else:
                            return False
                
        return True