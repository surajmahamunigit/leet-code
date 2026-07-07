class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        """
        Args:
            n: number of pairs of parenthesis

        Returns:
            list[]: list of all well-formed parenthesis

        Time: O(2**n) -
        Space: O(n) -
        """
        # Add "(" as long as open < n
        # Add ")" as long as close < open
        # if open == close == n

        result = []
        stack = []

        def backtracking(open_parenthesis, close_parenthesis):

            if open_parenthesis == close_parenthesis == n:
                result.append("".join(stack))
                return

            if open_parenthesis < n:
                stack.append("(")
                backtracking(open_parenthesis + 1, close_parenthesis)
                stack.pop()

            if close_parenthesis < open_parenthesis:
                stack.append(")")
                backtracking(open_parenthesis, close_parenthesis + 1)
                stack.pop()

        # call inner function
        backtracking(0, 0)
        return result

result = Solution().generateParenthesis(3)
print(result)