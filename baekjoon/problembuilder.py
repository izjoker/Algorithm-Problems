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
        f.write("from sys import stdin\ndef sol():\n\treturn\nn = int(stdin.readline().strip())\n")
    



    

def getproblem(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    driver.set_page_load_timeout(5)
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

# soup = bs(res.text, 'html.parser')
# print(soup.find_all(class_="container content"))

# https://www.acmicpc.net/problem/9252
# <pre class="sampledata" id="sample-input-1">ACAYKP
# CAPCAK
# </pre>

# 자, 이제 find_elements_by_css_selector( ) 함수로 chromedriver가 검색창을 찾을 수 있게 해봅시다.

# # 검색어 창을 찾아 search 변수에 저장 (css_selector 이용방식)
# search_box = driver.find_element_by_css_selector('input.gLFyf.gsfi')

# # 검색어 창을 찾아 search 변수에 저장 (xpath 이용방식)
# search_box = driver.find_element_by_xpath('//*[@id="google_search"]')
