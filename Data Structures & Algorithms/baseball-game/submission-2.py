class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for operation in operations:
            if operation == 'C':
                score_stack.pop()
            elif operation == 'D':
                prev_score = score_stack[-1]
                score_stack.append(2 * prev_score)
            elif operation == '+':
                prev_1 = score_stack[-1]
                prev_2 = score_stack[-2]
                score_stack.append(prev_1 + prev_2)
            else:
                score_stack.append(int(operation))

        return sum(score_stack)