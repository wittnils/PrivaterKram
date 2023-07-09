# methods to reverse a number and to check whether its a palindrome
def reverse(n):
    reversed_n = 0
    while n > 0:
        last_digit = n % 10
        reversed_n = reversed_n*10 + last_digit
        n = n//10
    return reversed_n

def check_palindrome(n):
    if n != reverse(n):
        return False
    else:
        return True

#actual implementation of the class
class transform:
    def __init__(self, value):
        self.value = value
        self.cycles = 0
    
    def palindrome(self):
        while((self.value <= 10**9) and (self.value >= 1)):
            if(check_palindrome(self.value)==True):
                return int(self.value)
            else:
                self.cycles += 1
                self.value += reverse(self.value)
        return -1
    def get_cycles(self):
        return int(self.cycles)