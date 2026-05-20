# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        graph = defaultdict(list)

        for a in range(n):
            for b in range(n):
                if a != b:
                    if knows(a, b):
                        graph[a].append(b)
        
        for person in range(n):
            if len(graph[person]) == 0:
                is_celi = True

                for other in range(n):
                    if person != other and not knows(other, person):
                        is_celi = False

                if is_celi:
                    return person

        return -1