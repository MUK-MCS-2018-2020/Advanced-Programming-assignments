# Jonathan Mukiibi:
# Registration Number: 2018/HD05/1968U
#
# Omara Patrick:
# Student Number:216018844
# Registration Number: 2016/HD05/339U
#
# Jerome Abura:
# Student Number: 203001168
# Registration Number: 2014/HD05/2094U
#
# Wabwire Robert:
# Student Number: 2018/HD05/1982U

import urllib.request
from bs4 import BeautifulSoup
import re


# Exercise 1A

print ('hello world')

# Numerical operations

def num_operations(num1,num2,num3,num4):
    numbers = (num1 - num2 * num3) / num4
    return numbers

print(num_operations(50,5,6,4))

# return the real and imaginary part of the complex number result in addition
def complex_num_operations(comp_num1,comp_num2):
    comp_result=comp_num1+comp_num2
    return 'The Real Part of the complex number is: '+ str(comp_result.real) +' the and Imaginary part: '+str(comp_result.imag)

print (complex_num_operations(1.5,0.5j))

# Strings, including string concatenation and indexing of characters.

def concate_strings(string_word1,string_word2):
    new_word = string_word1 + string_word2
    return new_word

print (concate_strings("Engineer","Baino"))

def index_last_char(name):
    last_char = name
    return last_char[-1:]

print(index_last_char("Jonathan"))

# Lists: how to construct them, access the elements, combine them.

def add_shopping_list_item(my_list,item_to_add):
    shopping_list=my_list
    shopping_list.append(item_to_add)
    return shopping_list

def remove_last_shopping_list_item(my_list):
    return my_list.pop()

my_list=['food','salt']
print(add_shopping_list_item(my_list,'cake'))
print(remove_last_shopping_list_item(my_list))

# Extend the Fibonnaci example so that each element in the sequence is stored in a list.
# return Fibonacci series up to n
def fibo_mcs(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)  # see below
        a, b = b, a + b
    return result


fib_nums_100 = fibo_mcs(100)  # call it
print(fib_nums_100)  # write the result


# Exercise 1B

def unique_words(string_word):
    return string_word.split()

print(unique_words('example string'))



#Exercise 2


def prime_numbers(number):
    for num in range(0, number + 1):
        # prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

prime_numbers(10)

# Exercise 3

# a helper function to remove html tags from a string
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# a function which retrieves a user's email address by requesting a web
# page from the Makerere staff directory
def find_telephone_number(name):
    name = name.lower()
    name = name.replace(' ','-')
    staffdirectorypage= urllib.request.Request('http://directory.mak.ac.ug/staff/%s.html' % (name))
    #staffdirectorypage = 'http://directory.mak.ac.ug/staff/%s.html' % (name)
    try:
        for line in urllib.request.urlopen(staffdirectorypage):
            if ('@' in line) and ('mak.ac.ug' in line) :
                line = remove_html_tags(line)
                return line
    except urllib.request.HTTPError:
        return 'Person not found'

# now call the above function to find some email addresses
for staffmember in ['John Ngubiri', 'Benjamin Kanagwa', 'John Quinn']:
    telephone_number = find_telephone_number(staffmember)
    print (telephone_number)


def dictionary(word_to_search):
    request = urllib.request.Request("http://www.dict.org/bin/Dict?Form=Dict2&Database=*&Query="+word_to_search)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find_all('pre')

print (remove_html_tags(str(dictionary('hacker'))))