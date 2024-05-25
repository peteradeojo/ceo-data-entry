import re
from datetime import datetime

namePattern = re.compile(r"\D", re.IGNORECASE)

def get_addresses(filename):
  f = open(filename)
  data = f.readlines()
  f.close()
  return data
  
def get_company_from_email(email: str):
  return email.split("@")

def parse_entry(entry: str):
  data = entry.strip().split(" ")
  return data[-1]

def remove_dot_com(address):
  return address.split(".")[0]

def get_companies(filename):
  return [get_company_from_email(parse_entry(x))[-1] for x in get_addresses(filename)]

def test_valid_name(name: str):
  l = len(name.split(" "))
  return l <= 3 and namePattern.match(name) is not None

def get_datetime():
  return datetime.now().strftime("%d-%m-%Y-%H:%M:%S")