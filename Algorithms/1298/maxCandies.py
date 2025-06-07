class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        boxes = set(initialBoxes)
        got_keys = set()
        got_candies = 0
        while True:
            can_open = {b for b in boxes if status[b] == 1 or b in got_keys}
            if not can_open:
                break
            for b in can_open:
                got_candies += candies[b]
                got_keys.update(keys[b])
                boxes.update(containedBoxes[b])
            boxes -= can_open
        return got_candies
