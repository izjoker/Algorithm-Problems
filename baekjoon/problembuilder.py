import os
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

def buildprob():
    print('Input Problem number:')
    probnum = input()
    if not probnum.isnumeric():
        print('Invalid input. Exiting.')
        return
    url = f'https://www.acmicpc.net/problem/{probnum}'
    html, stdin, stdout = getproblem(url)

    if os.path.exists(f"./{probnum}"):
        print('directory exists. Exiting.')
        return
        
    os.mkdir(f"./{probnum}")
    with open(f'./{probnum}/README.md', 'w', encoding="utf-8") as f:
        f.write(f"# {probnum} \n")
        f.write(f"Source URL: {url} \n")
        f.write(f"# Description \n")
        f.write(str(html))
    with open(f'./{probnum}/stdin', 'w', encoding="utf-8") as f:
        f.write(stdin)
    with open(f'./{probnum}/stdout', 'w', encoding="utf-8") as f:
        f.write(stdout)
    with open(f'./{probnum}/sol.py', 'w', encoding="utf-8") as f:
        f.write("from sys import stdin\ndef sol():\nreturn\nn = int(stdin.readline().strip())\n")
    



    

def getproblem(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    driver.set_page_load_timeout(60)
    try :
        driver.get(url)
        print("URL successfully Accessed")
    except Exception as e:
        print("Page load Timeout Occurred. Try again.")
        return
        
    soup = bs(driver.page_source)
    soup = soup.find(class_="container content")
    soup = soup.find(id="problem-body")
    probBody = str(soup)
    
    sampleIn = str(soup.find(id="sample-input-1").get_text())
    sampleOut = str(soup.find(id="sample-output-1").get_text())
    return [probBody, sampleIn, sampleOut]
    

buildprob()
