class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        n = len(boxes)
        answer = [-1] * n

        
        for i in range(len(boxes)):

            count = 0

            for j in range(len(boxes)):

                if i == j:
                    continue
                elif j < i:
                    if boxes[j] == '1':
                        count += (i-j)
                    else:
                        continue
                elif i < j:
                    if boxes[j] == '1':
                        count += (j-i)
                    else:
                        continue

            answer[i] = count

        return answer

