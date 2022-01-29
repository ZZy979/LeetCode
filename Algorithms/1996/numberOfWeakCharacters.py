class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda p: (-p[0], p[1]))
        num_weak = max_defense = 0
        for _, defense in properties:
            if defense < max_defense:
                num_weak += 1
            else:
                max_defense = max(max_defense, defense)
        return num_weak
