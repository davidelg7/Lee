import pickle

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep
file="logFile.csv"
import os
starting=0
if os.path.exists(file):
    f=open(file,"r")
    starting=int(f.readlines()[-1].split(",")[0])+1
try:
    f = open(file, "a")
except:
    f = open(file, "w")
    f.write("CODE,URL,VALIDITY\n")

notFixedLength=15
validCodes={}
fixed="SOP"

def extend(intCode):
    s=str(intCode)
    return "0"*(notFixedLength-len(s))+s
def buildCode(intCode):
    return fixed+extend(intCode)
def buildUrl(intCode):
    return "https://www.ninjavan.co/en-ph/tracking?id="+buildCode(intCode)
def isValid(html):
    return "Parcel Information" in html
def checkifValid(intCode):
    browser.get(buildUrl(intCode))
    sleep(3)
    try:
        html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        return isValid(html)
    except NoSuchElementException:
        sleep(1)
def checkAndSave(intCode):
    validity=checkifValid(intCode)
    print("Checked ",str(intCode)+",",buildUrl(intCode)+",",str(validity))
    f.write(str(intCode)+","+buildUrl(intCode)+","+str(validity)+"\n")
    f.flush()

from selenium.webdriver.chrome.options import Options


WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

browser = driver = webdriver.Chrome(executable_path='.\chromedriver.exe',options=chrome_options)

while len(str(starting))<=15:
    checkAndSave(starting)
    starting+=1

driver.close()