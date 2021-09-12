import string
import math
from functools import reduce
import  re

def unpack():
    T = (1, 2, "a", "b")
    L = ["hello", "there", "are", "some", "numbers", "coming", "from", "tuple"]
    print("Before unpacking the list is")
    print(L)
    L[0], L[1], L[2], L[3] = T
    print("After unpacking the list is")
    return L

def secondLargest(Tuple):
    
    T = len(Tuple)
    maxv = max(Tuple)
    secmax = 0
    for i in range(len(Tuple)):
        if secmax < Tuple[i] < maxv:
            secmax = Tuple[i]
    return secmax

def getPowers(x):
    
    T = (x, x**2, x**3, x**4)
    return T

def addTuple(t1, t2):
    t3 = t1 + t2
    return t3

def shortest(str_tuple):
    return len(min(str_tuple))

def createIntTuple(t):
    tpl = ()
    for i in range(t):
        tpl += (i,)
    return tpl

def strtuple():
    tpl = ()
    alpha = string.ascii_lowercase
    i = 1
    for char in alpha:
        tpl += (char*i,)
        i += 1
    return tpl

def fibonaccituple(n):
    tpl = ()
    tpl += (0,)
    tpl += (1,)
    a = 0
    b = 1
    for i in range(n-2):
        c = a+b
        tpl += (c,)
        a = b
        b = c
    return tpl

def returnValue(n, t):
    series = fibonaccituple(n)
    for i in range(len(series)):
        if series[i] == t:
            return i+1

def nestedTuple(n):
    tpl = ()
    for i in range(n):
        t = tuple(map(int, input().split()))
        tpl += (t,)

    return tpl

def calcAverage(n):
    tpl = nestedTuple(n)

    for i in range(len(tpl)):
        print("Average marks obtained by student {} is {}".format(i+1,sum(tpl[i])//len(tpl[i])))

def displayInfo(d):
    for key in d:
        print("Employee  {}".format(key))
        print("     Age:    {}".format(d[key]['age']))
        print("     Salary:    {}".format(d[key]['salary']))

def storeDetails(n):
    d = {}
    for i in range(n):
        
        for i in range(3):
            rollNo = int(input())
            d1 = {}
            d1['name'] = input()
            d1['marks'] = int(input())
            d1['grade'] = input()
            d[rollNo] = d1
        print(d)

def iplGames(n):
    d = {}
    for i in range(n):
        team_name = input()
        d1 = []
        win = int(input())
        lost = int(input())
        d1.append(win)
        d1.append(lost)
        d[team_name] = d1
    
    for key in d:
        print("Winning percentage for {} is {:.2f}%".format(key, (d[key][0]/sum(d[key]))*100))
        print("{} won {} matches".format(key, d[key][0]))
        #(d[key][0]/sum(d[key]))*100

def groceryStore(n):
    d = {}
    for i in range(n):
        product = input()
        price = int(input())
        d[product] = price
    print(d)
    q = input()
    print(d.get(q, "Error!!Product not found"))

def monthNames():
    month = {'january': 31, 'february':28, 'march':31, 'april':30, 'may':31, 'june':30, 'july':31, 'august':31, 'september':30, 
    'october':31, 'november':30, 'december':31}
    q = input("Enter  month name: ").lower()
    print("{} has {} days".format(q.upper(), month[q]))
    print("Printing keys in alphabetic orders......")
    
    for item in sorted(month.keys()):
        print(item)

    print("Printing all of the months with 31 days......")
    for key in month:
        if month[key] == 31:
            print(key, month[key])
    
    print("Printing key-value pairs sorted by days in each month......")
    for item in sorted(month.items(), key=lambda x : (x[1],x[0])):
        print(item)

def listNumbers(n):
    make_lst = []
    for i in range(n):
        num = int(input())  
        make_lst.append(num)
    print("List containing numbers: {}".format(make_lst))
    print("Replacing numbers greater than 10 with 10......")
    print([10 if x > 10 else x for x in make_lst])

def listStrings(n):
    make_lst = []
    for i in range(n):
        string = input() 
        make_lst.append(string)
    print("List containing numbers: {}".format(make_lst))
    print("Replacing numbers greater than 10 with 10......")
    new_lst = [x[1:] for x in make_lst]
    print("Old list....")
    print(make_lst)
    print("New list....")
    print(new_lst)

def usingLoops(n):
    print("Printing squares..........")
    print([i**2 for i in range(1, 50)])
    print("Printing alphabets..........")
    alpha = string.ascii_lowercase
    print([alpha[i]*i for i in range(len(alpha))])

def addList(l1, l2):
    l = []
    for i in range(len(l1)):
        l.append(l1[i]+l2[i])
    print(l)

def addListLambda(l1, l2):
    l = list(map(lambda x,y : x+y, l1, l2))
    print(l)

def rotateList(l, index):
    #[1,2,3,4,5,6]
    print(l[index:]+l[:index])

def createfibonacci(n):
    lst = []
    a = 0
    b = 1
    lst.append(a)
    lst.append(b)
    for i in range(n-2):
        c = a+b
        lst.append(c)
        a = b
        b = c
    print(lst)
    q = int(input())
    if q < n:
        print(lst[q])
    else:
        print("Number greater than n")

def pattern1(n):
    alpha = string.ascii_uppercase
    str1 = alpha[:n]
    for i in range(1,n+1):
        print("  ".join(list(alpha[:i])))

def pattern2(n):
    
    for i in range(1, n):
        print((" ".join(i*"*")).center(2*n-1, " "))
    print(" ".join(n*"*"))
    for i in range(n-1, 0, -1):
        print((" ".join(i*"*")).center(2*n-1, " "))

def pattern3(n):
    
    for i in range(1, n+1):
        print(" ".join(i*"*"))
    for i in range(n-1, 0, -1):
        print(" ".join(i*"*"))

def pattern4(n):
    if n%2 != 0:
        print((" ".join(1*"*")).center(2*n-1, " "))
        for i in range(1, n+2,2):
            print(((i*" ").join("**")).center(2*n-1, " "))       
        for i in range(n-2, 0, -2):
            print(((i*" ").join("**")).center(2*n-1, " "))
        print((" ".join(1*"*")).center(2*n-1, " "))
    else:
        print((" ".join(1*"*")).center(2*n-1, " "))
        for i in range(1, n+2,2):
            print(((i*" ").join("**")).center(2*n-1, " "))       
        for i in range(n-1, 0, -2):
            print(((i*" ").join("**")).center(2*n-1, " "))
        print((" ".join(1*"*")).center(2*n-1, " "))

def pattern5(n):
    print("*")
    for i in range(1, n+2):
        print((i*"  ").join("**"))
    for i in range(n, 0, -1):
        print((i*"  ").join("**"))
    print("*")

def avgList():
    lst = list(map(int, input().split()))
    print(sum(lst)/len(lst))

def drawRectangle(n,m):
    print("*"*m)
    for i in range(n-2):
        print("*"+(m-2)*" "+"*")
    print("*"*m)

def ascendingOrder(a,b,c):
    # if a < b and b < c:
    #     print("Smallest number={}".format(a))
    #     print("Next higher number={}".format(b))
    #     print("Highest number={}".format(c))
    # elif b < c and c < a:
    #     print("Smallest number={}".format(b))
    #     print("Next higher number={}".format(c))
    #     print("Highest number={}".format(a))
    # elif a < c and c < b:
    #     print("Smallest number={}".format(a))
    #     print("Next higher number={}".format(c))
    #     print("Highest number={}".format(b))
    # elif c < a and a < b:
    #     print("Smallest number={}".format(c))
    #     print("Next higher number={}".format(a))
    #     print("Highest number={}".format(b))

    if a < b < c:
        print("Smallest number={}".format(a))
        print("Next higher number={}".format(b))
        print("Highest number={}".format(c))
    elif b < a < c:
        print("Smallest number={}".format(b))
        print("Next higher number={}".format(a))
        print("Highest number={}".format(c))
    elif c < b < a:
        print("Smallest number={}".format(c))
        print("Next higher number={}".format(b))
        print("Highest number={}".format(a))
    elif a < c < b:
        print("Smallest number={}".format(a))
        print("Next higher number={}".format(c))
        print("Highest number={}".format(b))
    elif b < c < a:
        print("Smallest number={}".format(b))
        print("Next higher number={}".format(c))
        print("Highest number={}".format(a))
    elif c < a < b:
        print("Smallest number={}".format(c))
        print("Next higher number={}".format(a))
        print("Highest number={}".format(b))

def check_length():
    l = int(input("enter the length in centimeters:"))
    if l > 0:
        print(2.54*l)
    else:
        print("input is invalid")

def store_item(n):
    if n < 10:
        print("The total cost for the items {}".format(n*120))
    elif n >= 10 and n <= 99:
        print("The total cost for the items {}".format(n*100))
    else:
        print("The total cost for the items {}".format(n*70))

def close_numbers():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))   

    if round(abs(a-b), 3) == .001:
        print("Close")     
    else:
        print("Not Close")

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
                return leap
            else:
                return leap
            return leap
        leap = True
    
    return leap

def value_digit(n):
    words = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num  = str(n)
    
    str1 = ''
    for char in num:
        str1 += words[int(char)]

    print(str1)

def prime_num_reverse(n):
    total = 0
    lst = []
    for i in range(2, 1000):
        num  = i
        cnt = 0
        for j in range(1, num+1):
            if num%j == 0:
                cnt += 1
        if cnt == 2:
            if total < n:

                lst.append(num)
                total += 1
    
    for  i in range(len(lst)-1, -1, -1):
        print(lst[i])

def prime_square_root(n):
    a = int(math.sqrt(n))
    b = 0 
    for i in range(2, a):
        if a%i == 0:
            b += 1
    if b == 0:
        print("{} is a prime number".format(a))
    else:
        print("{} is not a prime number".format(a))

def avg_list_numbers():
    lst = list(map(int, input().split()))
    print(sum(lst)/len(lst))

def largest_number():
    lst = list(map(int, input().split()))
    maxval = 0
    for  i in range(len(lst)):
        if lst[i] > maxval:
            maxval = lst[i]
    print("Maximim number in the list is {}".format(maxval))

def num_palindrome(n):
    num = str(n)
    if num == num[::-1]:
        print("{} is a palindrome".format(n))
    else:
        print("{} is not a palindrome".format(n))

def form_number(n):
    if n > 100:
        ld = n % 10
        while n >= 10:
            n = n // 10
        
        if ld != 0:
            print(str(ld)+str(n))
        else:
            print("forming number is not possible")
    else:
        print("Invalid number")

def divisible_m(n, m):
    for i in range(1, n):
        if i % m == 0:
            if i % 2 == 0:
                print("{} is divisible by m and {} is an even number".format(i,i))
            else:
                print("{} is divisible by m and {} is an odd number".format(i,i))

def age_list(lst):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(len(lst)):
        if lst[i] >= 26 and lst[i] <= 35:
            cnt1 += 1
        elif lst[i] >= 36 and lst[i] <= 45:
            cnt2 += 1
        elif lst[i] >= 46 and lst[i] <= 55:
            cnt3 += 1

    print("Number of e employees in the age group (26-35):{}".format(cnt1))
    print("Number of e employees in the age group (36-45):{}".format(cnt2))
    print("Number of e employees in the age group (46-55):{}".format(cnt3))

def add_str_digit(num1, str1):
    num2 = ''
    for char in str1:
        if char.isdigit():
            num2 += char
    if len(num2) == 0: 
        print(num1) 
    else:  
        print(int(num1)+int(num2))

def create_pattern(str1):
    s = " ".join(list(str1))
    spacing = len(s)    
    j = 2
    for i in range(0, (len(s)+1)//2, 2): 
        if i != len(s)-1-i:      
            d = s[i]+' '*(len(s)-j)+s[len(s)-1-i]
            j += 4       
            print(d.center(spacing, ' '))
        else:
            d = s[i]
            print(d.center(spacing, ' '))

def cmp_string(str1, str2):    
    if  str1 > str2:
        print(str2)
        create_pattern(str1)
    else:
        print(str1)

        create_pattern(str2)

def convert_case_sentence(lines):
    for line in lines:
        str1 = ''
        for char in line:
            
            if char.islower():
                str1 += char.upper()
            elif char.isupper():
                str1 += char.lower()
            else:
                str1 += char.lower()

        print(str1)


def convert_case():
    lst = []
    
    for i in range(100):  
        s = input("Please enter a sentence, or 'q' to quit:")      
        sentence = input()

        if sentence == 'q' or sentence == 'Q':
            break
        
        lst.append(sentence)

        
    convert_case_sentence(lst)

def word_count(s):    
    return len(s.split())

def character_count(s):
    return len(s)

def alphanumeric(s):
    cnt = 0
    for char in s:
        if char.isalnum():
            cnt += 1
    perc = round((cnt/len(s))*100, 2)
    return perc
    

def word_statistics():

    sentence = input()
    wordcount = word_count(sentence)
    print("Total word count in a sentence is {}".format(wordcount))
    charactercount = character_count(sentence)
    print("Total character count in a sentence is {}".format(charactercount))
    alpha = alphanumeric(sentence)
    print("Percentage of characters that are alpha-numeric: {} %".format(alpha))

def digit_count(s):
    d = ''
    for char in s:
        if char.isdigit():
            d += char
    if len(d) > 0:
        return d
    return 0

def string_digit():
    s = input()
    dcnt = digit_count(s)
    if dcnt:
        sum1 = reduce(lambda x, y: x+y, [int(x) for x in dcnt])
        print("Original string is {} has digits {} which sum to {}".format(s, dcnt, sum1))
    else:
        print("Original string is {} has no digits".format(s))

def valid_numbers(s):
    
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.search(pattern, s):
        print("{} is a valid phone number".format(s))
    else:
        print("{} is not a valid phone number".format(s))
    

    
        
    


    

        


    


    




        






    













    
# print(unpack())
# print(secondLargest((23, 45, 34, 66, 77, 67, 70)))
# print(getPowers(2))
# print(addTuple((1, 2, 3),(4, 5, 6)))
# print(shortest(('Ambfg', 'xyz', '123', 'abcd')))\
# print(createIntTuple(50))
# print(strtuple())
# print(fibonaccituple(9))
# print(returnValue(9,3))
# print(nestedTuple(5))
# calcAverage(5)
# Employees = {'John':{'age': 25, 'salary':2000}, 'Diya':{'age':35, 'salary':50000}}
# displayInfo(Employees)
# storeDetails(2)
# iplGames(2)
#groceryStore(2)
# monthNames()
# listNumbers(12)
# listStrings(5)
# usingLoops(50)
# addList([3,1,4],[1,5,9])
# addListLambda([3,1,4],[1,5,9])
# rotateList([1,2,3,4,5,6],3)
# createfibonacci(26)
# pattern1(7)
# drawRectangle(8,50)
# avgList()
# pattern2(7)
# pattern3(7)
# pattern4(9)
# pattern5(8)
# ascendingOrder(1,3,2)
# check_length()
# store_item(100)
# close_numbers()
# print(is_leap(1990))
# value_digit(8910)
# prime_num_reverse(9)
# prime_square_root(16)
# avg_list_numbers()
# largest_number()
# num_palindrome(569)
# form_number(987)
# divisible_m(50, 3)
# age_list([27, 37, 44, 31, 51, 49, 55, 50, 52, 30, 38, 39])
# add_str_digit(100, 'hi mom')
# cmp_string('PROGRAM', 'Python')
# convert_case()
# word_statistics()
# string_digit()
valid_numbers('017-555-1212')




