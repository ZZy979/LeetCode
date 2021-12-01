from collections import Counter, defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_food = defaultdict(Counter)
        all_food = set()
        for _, table_no, food in orders:
            table_food[int(table_no)][food] += 1
            all_food.add(food)
        all_food = sorted(all_food)
        return [['Table'] + all_food] + [
            [str(table_no)] + [str(table_food[table_no][food]) for food in all_food]
            for table_no in sorted(table_food)
        ]
