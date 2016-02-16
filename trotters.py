#!/usr/bin/env python
# int to word. codetrotters
# Alejandro Salvador Vega Nogales, vega360@gmail.com, git: asvnpr
def intToWord(n):
    if (n == 0):
        return "zero"
    else:
        # commence string building and component declaration
        ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine" }
        teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14:"fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
        tens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety" }
        others = ["hundred", "thousand", "million"]
        digits = []
        build = []
        word = ""
        numStr = str(n) #convert int num to String
        l = len(numStr)

        #capture all digits in int n in a list
        for i in range(0, len(numStr)):
            digits.append(int(numStr[i]))

        # go through list and convert digits to words and build the string
        teen = False
        while (l > 0):
            #10^8 to 10^6
            if (l == 9):
                if (digits[-l] != 0 or digits[-(l - 1)] != 0):
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append("and")
                else:
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append(others[2])
            elif (l == 8 and digits[-l] != 0):
                if (digits[-(l - 1)] != 0):
                    build.append(tens[digits[-l]])
                else:
                    build.append(tens[digits[-l]]), build.append(others[2])
            elif (l == 7 and digits[-l] != 0):
                    build.append(ones[digits[-l]]), build.append(others[2])
            #10^5 to 10^3
            elif (l == 6 and digits[-l] != 0):
                if (digits[-(l - 1)] != 0 or digits[-(l - 2)] != 0):
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append("and")
                else:
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append(others[1])
            elif (l == 5 and digits[-l] != 0):
                if (digits[-(l - 1)] != 0):
                    build.append(tens[digits[-l]])
                else:
                    build.append(tens[digits[-l]]), build.append(others[1])
            elif (l == 4 and digits[-l] != 0):
                    build.append(ones[digits[-l]]), build.append(others[1])
            #10^2 to 10^0
            elif (l == 3 and digits[-l] != 0):
                if (digits[-(l - 1)] != 0 or digits[-(l - 2)] != 0):
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append("and")
                else:
                    build.append(ones[digits[-l]]), build.append(others[0])
            elif (l == 2 and digits[-2] == 1 and digits[-1] > 0 and teen == False):
                tmp = digits[len(digits) - 1] + 10
                build.append(teens[tmp])
                teen = True
            elif (teen != True):
                if (l == 2 and digits[-l] != 0):
                    if (digits[-(l - 1)] != 0):
                        build.append(tens[digits[-l]])
                    else:
                        build.append(tens[digits[-l]])
                elif (l == 1 and digits[-l] != 0):
                    build.append(ones[digits[-l]])
            l -= 1
        word = ' '.join(build)
        return word

n = int(raw_input("Enter a whole number between 0 and 999,999,999: "))
while (n > 999999999 or n < 0):
    print "Error! You entered a value that was too large or too small."
    n = int(raw_input("Please enter a whole number between 0 and 999,999,999: "))
print intToWord(n)










