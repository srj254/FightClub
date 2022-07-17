#!/usr/bin/python3 

import finterface
import pprint 

global method

def create_new_user():
  fn = input("First name: ")
  ln = input("Last name: ")

  entity = finterface.method.entities.create({
    'type': 'individual', 
    'individual': {
      'first_name': fn,
      'last_name': ln,
      'phone': '+16505555555',
      'email': 'kevin.doyle@gmail.com',
      'dob': '1997-03-18',
    },
    'address': {
      'line1': '3300 N Interstate 35',
      'line2': None,
      'city': 'Austin',
      'state': 'TX',
      'zip': '78705'
    }
  })
  print (entity.id); 
  return entity; 

def get_users(): 
  for e in finterface.method.entities.list(): 
    print ("="*80); 
    pprint.pprint(e); 
  
