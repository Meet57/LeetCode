class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))  # store tuples of (timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        # Perform binary search manually to find the largest timestamp <= given timestamp
        left, right = 0, len(values) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            mid_timestamp, mid_value = values[mid]
            
            if mid_timestamp == timestamp:
                return mid_value  # If exact match found
            elif mid_timestamp < timestamp:
                result = mid_value  # Keep track of last valid value
                left = mid + 1  # Look in the right half
            else:
                right = mid - 1  # Look in the left half
        
        return result  # If no exact match, return the last valid value
