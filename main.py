from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

os.system('pip install pyperclip')
os.system('pip install selenium')





print("""
   / / / / //_// ____/\ \/ /             / / / / / / /  |/  / __ \/ __ \   <  /
  / /_/ / ,<  / __/    \  /  ______     / /_/ / / / / /|_/ / / / / /_/ /   / / 
 / __  / /| |/ /___    / /  /_____/    / __  / /_/ / /  / / /_/ / _, _/   / /  
/_/ /_/_/ |_/_____/   /_/             /_/ /_/\____/_/  /_/\____/_/ |_|   /_/   """)

print('Tüm kütüphaneleri yükledik.')

driver_path = 'chromedriver.exe'
browser = webdriver.Chrome(driver_path)
action = webdriver.ActionChains(browser)

usrnm = input('Username gir :')
pswd = input('Şifresi gir:')
browser.get("https://www.instagram.com/")
time.sleep(5)

a = browser.find_element_by_name('username')
b = browser.find_element_by_name('password')


a.send_keys(usrnm)
b.send_keys(pswd+ Keys.ENTER)

time.sleep(4)

hedef = input('Hedef hesap giriniz:')
browser.get('https://www.instagram.com/' + hedef)

time.sleep(4)
dakipci = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(5)

dialog = browser.find_element_by_css_selector("div[role=dialog] ul")
time.sleep(5)

takip_etmedigin_kisiler,ent,takip,sayac = 0,0,0,1

while True:
    tkpci = len(dialog.find_elements_by_css_selector("li"))
    takip_et = browser.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{sayac}]/div/div[3]')
    metin = browser.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{sayac}]/div/div[3]/button').text
    if ent == int(tkpci)- takip_etmedigin_kisiler:
        print('Bitti. Git kumda oyna')
        break
    if metin == 'Takiptesin' or metin == 'İstek Gönderildi':
        print(metin)
        sayac+=1
        takip_etmedigin_kisiler +=1
        continue
    takip_et.click()
    dialog.click()
    action.key_down(Keys.SPACE)
    takip+=1
    sayac+=1
    ent+=1
    time.sleep(1)
    if takip == 10:
        takip=0
        time.sleep(5)
        dialog.click()
        action.key_down(Keys.SPACE)




