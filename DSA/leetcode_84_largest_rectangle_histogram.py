class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_smallest = self.left_smallest(
            heights
        )
        ans = float("-inf")
        right_smallest= self.right_smallest(heights)
        width = [0]*n
        for i in range(n):
            width[i] = right_smallest[i] - left_smallest[i] - 1

            area = width[i] * heights[i]

            ans = max(area, ans)
        
        return int(ans)


    def left_smallest(self, heights):
        n = len(heights)
        st = []
        answer = [-1] * n
        for i in range(n):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if len(st) == 0:
                answer[i] = -1
            else:
                answer[i] = st[-1]
            st.append(i)
        return answer

    def right_smallest(self, heights: List[int]):
        n = len(heights)
        st = []
        answer = [-1] * n

        for i in range(n-1,-1,-1):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if len(st) == 0:
                answer[i] = n
            else:
                answer[i] = st[-1]
            st.append(i)
        return answer
    



# Optimal 
def largestRectangleArea(self, heights):
    n = len(heights)
    st = []
    ans = float("-inf")
    for i in range(n):
        while len(st) > 0 and heights[st[-1]] >= heights[i]:
            j = st.pop()
            left = st[-1] if st else -1
            area =  ( i - left -1) *heights[j]
            ans = max(area, ans)
        st.append(i)
    
    while  len(st) != 0:
        j = st.pop()
        left = st[-1] if st else -1

        area =  ( n - left -1) *heights[j]
        ans = max(area, ans)
    return ans
            
