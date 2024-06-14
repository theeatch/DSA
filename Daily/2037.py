from pysvt import test

d={
    "i": [[[3,1,5],[2,7,4]],[[4,1,5,9],[1,3,2,6]]],
    "o": [4, 7],
}

@test(data=d, method="minMove")

class Solution:
    def minMove(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        moves=0
        for i in range(len(seats)):
                moves+= abs(seats[i]-students[i])
        return moves