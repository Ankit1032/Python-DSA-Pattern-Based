class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        visited.add(n)

        while n != 1:
            n = self.sum_of_squares(n)

            if n in visited:
                return False
            visited.add(n)

        return True

    def sum_of_squares(self,n):

        res = 0

        while n>0:
            temp = n%10
            res += (temp*temp)
            n = n//10

        return res
