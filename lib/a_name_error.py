#!/usr/bin/env python3

# print("hello_world")
def greet_programmer():
    print ('Hello,programmer')

greet_programmer()

def greet(name):
    print(f"Hello,{name}")

greet("Jerry")

def greet_with_default(name='programmer'):
    print(f'Hello,{name}')
greet_with_default('Ambwere')    

def add(sum1,sum2):
    print (sum1 + sum2)
add(2,3)

def halve(num):
    print (num/2)
halve(100)