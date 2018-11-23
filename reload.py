# -*- coding: utf-8 -*-
from __future__ import division
import mysql.connector
from selenium import webdriver
import math,time

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='l2db')
cnx2 = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='l2db')
cursor=cnx.cursor()
cursor.execute("SELECT sourse.id,sourse.name,items.link FROM sourse INNER JOIN items ON sourse.name=items.name ORDER BY id;")
driver=webdriver.Firefox(executable_path=r"d:/Python27/selenium/webdriver/geckodriver.exe")
driver.set_window_size(1200, 700)

for j in cursor:
    driver.get("https://l2central.info"+j[2])

    time.sleep(2)
    try:
        price = driver.find_element_by_xpath("//table[@id='item_brief_info_2']").find_element_by_css_selector(
        "tbody").find_elements_by_css_selector("tr")

        if len(price)>2:
            price = price[2:]
        price = [i for i in price if i.find_element_by_css_selector("td").text == u"Базовая цена:"]
        price = price[0].find_elements_by_css_selector("td")
        price = price[1].text
        price = price[:price.find(u"\u0430") - 1]
        price = int(price.replace(',',''))
        if price=='': price=0
        driver.find_element_by_link_text(u"Рынок").click()
    except:
        price=0
    print price
    try:
        buy = driver.find_element_by_xpath("//div[@data-market-type='buys']").find_elements_by_css_selector("table")
        try:
            buy_ei = buy[0].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            buy_ei = buy_ei[2].find_element_by_css_selector("td").text
            buy_ei = buy_ei.replace(' ','')
        except: buy_ei = round(math.ceil(price/2))
        try:
            buy_pa = buy[1].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            buy_pa = buy_pa[2].find_element_by_css_selector("td").text
            buy_pa = buy_pa.replace(' ','')
        except: buy_pa = round(math.ceil(price/2))
        try:
            buy_gk = buy[2].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            buy_gk = buy_gk[2].find_element_by_css_selector("td").text
            buy_gk = buy_gk.replace(' ','')
        except: buy_gk = round(math.ceil(price/2))
        try:
            buy_sh = buy[3].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            buy_sh = buy_sh[2].find_element_by_css_selector("td").text
            buy_sh = buy_sh.replace(' ', '')
        except: buy_sh = round(math.ceil(price/2))
    except:  buy_gk=buy_sh=buy_ei=buy_pa=round(math.ceil(price/2))
    try:
        sell = driver.find_element_by_xpath("//div[@data-market-type='sells']").find_elements_by_css_selector("table")
        try:
            sell_ei = sell[0].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            sell_ei = sell_ei[2].find_element_by_css_selector("td").text
            sell_ei = sell_ei.replace(' ', '')
            if sell_ei == '': sell_ei = 0
        except:
            sell_ei = round(math.ceil(price / 2))
        try:
            sell_pa = sell[1].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            sell_pa = sell_pa[2].find_element_by_css_selector("td").text
            sell_pa = sell_pa.replace(' ', '')
            if sell_pa == '': sell_pa = 0
        except:
            sell_pa = round(math.ceil(price / 2))
        try:
            sell_gk = sell[2].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            sell_gk = sell_gk[2].find_element_by_css_selector("td").text
            sell_gk = sell_gk.replace(' ', '')
            if sell_gk == '': sell_gk = 0
        except:
            sell_gk = round(math.ceil(price/2))
        try:
            sell_sh = sell[3].find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
            sell_sh = sell_sh[2].find_element_by_css_selector("td").text
            sell_sh = sell_sh.replace(' ', '')
            if sell_sh == '': sell_sh = 0
        except:
            sell_sh = round(math.ceil(price/2))
    except:
       sell_gk=sell_sh=sell_ei=sell_pa=round(math.ceil(price/2))

    cursor2 = cnx2.cursor()

    cursor2.execute(("UPDATE items SET buy_ei=%s,buy_pa=%s,buy_gk=%s,buy_sh=%s,sell_ei=%s,sell_pa=%s,sell_gk=%s,sell_sh=%s WHERE name=%s") ,(buy_ei,buy_pa,buy_gk,buy_sh,sell_ei,sell_pa,sell_gk,sell_sh,j[1]))
    cnx2.commit()

    print buy_ei,sell_ei
cursor.close()
cnx.close
cnx2.close
driver.close()
