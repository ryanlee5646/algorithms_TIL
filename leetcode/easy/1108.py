# 1108. Defanging an IP Address

# class Solution(object):
#     def defangIPaddr(self, address):
#         address = address.replace('.','[.]')
#         return address

# class Solution(object):
#     def defangIPaddr(self, address):
#         result = ''
#         for i in address:
#             if i == '.':
#                 result += '[.]'
#             else:
#                 result += i
#         return result

class Solution(object):
    def defangIPaddr(self, address):
        return '[.]'.join(address.split('.'))