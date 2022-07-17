#!/usr/bin/python3 

import os 
import sys  
import pprint

import user 
import account 
import schedule
import finterface

if __name__ == "__main__":
  
  print (finterface.API_KEY)
  print (str(finterface.method))

  api_dict = {
    'New User'                    : user.create_new_user,
    'Get User'                    : user.get_users,

    'New Source Accounts'         : account.add_src_acc,
    'Get Source Accounts'         : account.get_src_accs, 
 
    'New Liability Accounts'      : account.add_dest_acc,
    'Get Liability Accounts'      : account.get_dest_accs, 
 
    'Schedule Payment'            : schedule.schedule_payment,
    'Get Payment schedules'       : schedule.get_payment_schedules
  }; 

  while True: 
    print ("What do you want to do?")
    actions = list(api_dict.keys())
    for i, action in enumerate(actions): 
      print ("{}. {}".format(i+1, action))  
    choice = input('Please enter your choice [q to quit]')
    choice = choice.strip(); 

    if choice == 'q': 
      exit()

    op = api_dict.get(actions[int(choice) - 1])
    if op: 
      op(); 
    else: 
      print ("Incorrect input value")
    continue
