class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        non_incr_before = [0] * len(security)
        non_decr_after = [0] * len(security)
        for i in range(1, len(security)):
            non_incr_before[i] = non_incr_before[i - 1] + 1 if security[i - 1] >= security[i] else 0
        for i in range(len(security) - 2, -1, -1):
            non_decr_after[i] = non_decr_after[i + 1] + 1 if security[i + 1] >= security[i] else 0
        return [i for i in range(len(security)) if non_incr_before[i] >= time and non_decr_after[i] >= time]
