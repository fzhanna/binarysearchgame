#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 20:52:15 2018

@author: fadyhanna
"""

print("Please think of a number between 0 and 100!")
low=0
high=100
ans=(int((low+high)/2))
print("Is your secret number "+str(ans)+"?")
r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while r=="l"or r=="h":
    while r=="l":
        low= ans
        ans=(int((low+high)/2))
        print("Is your secret number "+str(ans)+"?")
        r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while r=="h":
        high=ans
        ans=(int((low+high)/2))
        print("Is your secret number "+str(ans)+"?")
        r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while r!="c" and r!="h" and r!="l":
        print("Sorry, I did not understand your input.")
        print("Is your secret number "+str(ans)+"?")
        r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while r!="l"and r!="h" and r!="c":
    print("Sorry, I did not understand your input.")
    print("Is your secret number "+str(ans)+"?")
    r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while r=="l":
        low= ans
        ans=(int((low+high)/2))
        print("Is your secret number "+str(ans)+"?")
        r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while r=="h":
        high=ans
        ans=(int((low+high)/2))
        print("Is your secret number "+str(ans)+"?")
        r=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while r=="c":
    print("Game over. Your secret number was: "+ str(ans))
    break