class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 360 / 60 = 6' each, minute
        # x = (min * 30)/60, hour*30 + x

        min_angle = minutes * 6
        if hour == 12:
            hour = 0
        hour_angle = hour*30 + ((minutes*30)/60)

        diff = abs(min_angle - hour_angle)

        print(min_angle, hour_angle)

        if diff > 180:
            return 360 - diff
        
        return diff