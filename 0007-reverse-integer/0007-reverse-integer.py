class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        
        # Remove leading zeros before conversion
        cleaned_str = reversed_str.lstrip('0') or '0'
        
        reversed_num = int(cleaned_str) * sign
        
        # Proper 32-bit boundary check
        if -2**31 <= reversed_num <= 2**31 - 1:
            return reversed_num
        return 0
        # if x > 0:
        #     x = str(x)[::-1]
        #     return int(x)
        # else:
        #     x = x * -1
        #     x = str(x)
        #     x = str(x)[::-1]
        #     x = int(x)*-1
        #     if -2**31 <= x <= 2**31 :
        #         return x  
        #     else:
        #         return 0
        