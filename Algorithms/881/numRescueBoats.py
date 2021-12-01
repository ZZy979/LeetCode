class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boats = 0
        i, j = 0, n - 1
        while i <= j:
            if i <= j and people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
