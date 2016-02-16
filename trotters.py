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
        teen = False #used for preventing
        while (l > 0):
            #10^8 to 10^6
            if (l == 9):
                if (digits[-(l - 1)] != 0 or digits[-(l - 2)] != 0):
                    print l-1
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append("and")
                else:
                    build.append(ones[digits[-l]]), build.append(others[0]), build.append(others[2])
            elif (l == 8 and digits[-8] == 1 and digits[-7] > 0): #10^4 is < 20,000,000 and > 10,000,000
                tmp = digits[-7] + 10
                build.append(teens[tmp]), build.append(others[2])
                teen = True
            elif (teen != True and (l == 8 or l == 7)): #10^4 is not < 20,000,000 and > 10,000,000
                if (l == 8 and digits[-l] != 0):
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

            elif (l == 5 and digits[-5] == 1 and digits[-4] > 0): #10^4 is < 20,000 and > 10,000
                tmp = digits[-4] + 10
                build.append(teens[tmp]), build.append(others[1])
                teen = True

            elif (teen != True and (l == 5 or l == 4)): #10^4 is not < 20,000 and > 10,000
                if (l == 5 and digits[-l] != 0):
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

            elif (l == 2 and digits[-2] == 1 and digits[-1] > 0): #cases where 10^1 is < 20 and > 10
                tmp = digits[-1] + 10
                build.append(teens[tmp])
                teen = True

            elif (teen != True and (l == 2 or l == 1)): #10^1 is not < 20 and > 10
                if (l == 2 and digits[-l] != 0):
                    if (digits[-(l - 1)] != 0):
                        build.append(tens[digits[-l]])
                    else:
                        build.append(tens[digits[-l]])
                elif (l == 1 and digits[-l] != 0):
                    build.append(ones[digits[-l]])
            l -= 1
        teen = False #reset teen bool in cases where n is of form #15,#15,#15 or similar
        word = ' '.join(build) #add spaces between words and save the completed string
        return word

n = int(raw_input("Enter a whole number between 0 and 999,999,999: "))
while (n > 999999999 or n < 0):
    print "Error! You entered a value that was too large or too small."
    n = int(raw_input("Please enter a whole number between 0 and 999,999,999: "))
print intToWord(n)
