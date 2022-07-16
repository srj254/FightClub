#!/usr/bin/python3 

import os 
import sys  
import pprint
from method import Method

def create_new_user(input_dict):
  print (input_dict) 
  return

def add_src_acc(input_dict): 
  print (input_dict) 
  return

def add_dest_acc(input_dict): 
  print (input_dict) 
  return

def schedule_payment(input_dict): 
  print (input_dict) 
  return

if __name__ == "__main__":

  create_new_user_inp   = {'new_user': None}
  add_src_acc_inp       = {'src_account': None}
  add_dest_acc_inp      = {'dest_account': None} 
  schedule_payment_inp  = {'schedule_payment': None}
  actions = {
    '1': (create_new_user, create_new_user_inp),
    '2': (add_src_acc, add_src_acc_inp),
    '3': (add_dest_acc, add_dest_acc_inp), 
    '4': (schedule_payment, schedule_payment_inp)
  }; 

  while True: 
    print ("What do you want to do?")
    print ("1. Create a new user")
    print ("2. Add a payment account")
    print ("3. Add a liability account")
    print ("4. Schedule a payment")
    choice = input('Please enter your choice [q to quit]')
  
    op = actions.get(choice)
    if choice == 'q': 
      exit()
    elif op: 
      op[0](op[1])
    else: 
      print ("Incorrect input value")
    continue
