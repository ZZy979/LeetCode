class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n
        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats
        return list(accumulate(diff))
