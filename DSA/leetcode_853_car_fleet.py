class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []

        pairs = sorted(zip(position, speed), reverse=True)

        for position, speed in pairs:
            time = (target - position) / speed
            if len(st) == 0:
                st.append(time)

            else:
                if st[-1] < time:
                    st.append(time)
            
        return len(st)
    
    