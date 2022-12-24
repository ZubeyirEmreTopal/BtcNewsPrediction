#VERİ TOPLAMA İŞLEMLERİ
from numpy import size
from selenium import webdriver
import time
import pyautogui as au

driver=webdriver.Chrome()
driver.get("https://tr.investing.com/crypto/bitcoin/news/1037")
file=open ("haberler.txt","a",encoding="utf-8")
time.sleep(3)
sayfa=1037
while True:
    for i in range(1,16):
    #ana sayfa haberlere tıklama
        a=0
        while True:
            a=a+1
            try:
                time.sleep(0.5)
                if a==10:
                    i=i+1
                driver.find_element_by_xpath(f'//*[@id="fullColumn"]/div[7]/div[3]/div[1]/article[{str(i)}]/div[1]/a').click()
                break
            except:
                print('burda1')
    #ekran değiştirme ileri
        while True:
            try:
                p = driver.current_window_handle
                chwd = driver.window_handles
                for w in chwd:
                    if(w!=p):
                        driver.switch_to.window(w)
                        break
                break
            except:
                print('burda2')
    #haber içeriği okuma
        b=0
        while True:
            time.sleep(0.5)
            b=b+1
            if b==20:
                break
            try:
                tarih=driver.find_element_by_xpath('//*[@id="leftColumn"]/div[1]/span').text
                file.write(f'{sayfa}.-->{i}.haber')
                file.write('\n')
                file.write(tarih)
                file.write('\n')
                for j in range(1,50):
                    try:
                        paragraf=driver.find_element_by_xpath(f'//*[@id="leftColumn"]/div[3]/p[{str(j)}]').text
                        file.write(paragraf)
                    except:
                        pass
                file.write('\n\n')
                driver.close()
                break
            except:
                print('burda3')
    #ekran değiştirme geri  
        c=0
        while True:
            time.sleep(0.5)
            if c==20:
                break
            try:
                p = driver.window_handles
                for w in chwd:
                    if(p!=w):
                        driver.switch_to.window(w)
                        break
                break
            except:
                print('burda4')
    #sayfa ilerletme
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="paginationWrap"]/div[3]/a').click()
            sayfa=sayfa+1
            break
        except:
            print('burda5')