'''
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, 
separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). 
For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. 
Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, 
so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. 
For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

 

Example 1:

Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

IP consists only of English letters, digits and the characters "." and ":".
'''

#自己想的 36ms, time complexity O(1), space complexity O(1)
#思路: 利用split(".") and split(":") 來初步區分是IPv4 還是 IPv6, 再個別詳細確認是否符合該區條件
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(IP.split(".")) == 4:
            for num in IP.split("."):
                if len(num) == 0:
                    return "Neither"
                if len(num) > 1 and num[0] == "0": #no leading zero
                    return "Neither"
                for i in range(len(num)):
                    if not num[i].isdigit():
                        return "Neither"
                if int(num) > 255:
                    return "Neither"
            return "IPv4"
        
        elif len(IP.split(":")) == 8:
            for num in IP.split(":"):
                if len(num) > 4 or len(num) == 0:
                    return "Neither"
                for i in range(len(num)):
                    if not num[i].isdigit():
                        if num[i].lower() not in ["a","b","c","d","e","f"]:
                            return "Neither"
            return "IPv6"
        
        return "Neither"

#自己重寫第二次, time complexity O(1), space complexity O(1)
class Solution:
    def validIPAddress(self, IP: str) -> str:
        if len(IP.split(".")) == 4:
            for num in IP.split("."):
                if len(num) == 0:
                    return "Neither"
                elif len(num) > 1 and num[0] == "0":
                    return "Neither"
                for d in num:
                    if not d.isdigit():
                        return "Neither"
                if int(num) > 255:
                    return "Neither"
            return "IPv4"
        
        elif len(IP.split(":")) == 8:
            for num in IP.split(":"):
                if not 1 <= len(num) <= 4:
                    return "Neither"
                for d in num:
                    if not d.isdigit() and d.lower() not in ["a", "b", "c", "d", "e", "f"]:
                         return "Neither"
            return "IPv6"
        return "Neither"
























