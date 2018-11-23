from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import msvcrt
import grab
import mysql.connector

class Item:
    def __init__(self, Info,mind,type):
        self.Name=Info[0][1].text
        self.Link=Info[0][1].attrib['href']
        cuantity=Info[1].text
        self.min=cuantity[:cuantity.find(u"\u2014")]
        self.max=cuantity[cuantity.find(u"\u2014")+2:]
        if self.max == "\n": self.max = self.min
        #self.count=(int(self.min)+int(self.max))/2

        self.Chance=Info[2].text
        self.Chancemin=self.Chance[1:self.Chance.find(u"\u2014")-2]
        self.Chancemax = self.Chance[self.Chance.find(u"\u2014")+2:len(self.Chance)-2]
        self.Chancemax=self.Chancemax.strip('~, ')
        if (self.Chancemin == "")or(self.Chancemin[0]=="~"): self.Chancemin = self.Chancemax
        self.Chance=(float(self.Chancemin)+float(self.Chancemax))/2
        print mind,self.Name,self.Link,"min=",self.min,"max=",self.max,"cmmin=",self.Chancemin,"cmax=",self.Chancemax#,(self.Chancemin+self.Chancemax)/2#self.count,self.Chance,
        cursor.execute('INSERT INTO loot (npc_id,item_name,item_link,min_i,max_i,chance,type) VALUES (%s,%s,%s,%s,%s,%s,%s)', (mind, self.Name, self.Link,self.min,self.max,self.Chance,type))
        cnx.commit()




class monster:
    def __init__(self, Info):
        self.Name=Info.find_element_by_css_selector("a").text
        self.Link=Info.find_element_by_css_selector("a").get_attribute("href")
        global ind
        drop=grab.Grab()
        try:drop.go(self.Link)
        except:print ("disconnect")
        self.lvl=0
        try:
            self.lvl = drop.xpath("//table[@id='npc_brief_info_2']")[3][1][0].text
            self.drop1=drop.xpath("//div[@id='mw-content-text']")[6][1:]
            self.drop1=[Item(i,ind,1) for i in self.drop1]
            self.drop2 = drop.xpath("//div[@id='mw-content-text']")[7][1:]
            self.drop2 = [Item(i,ind,1) for i in self.drop2]
            self.Spoil = drop.xpath("//div[@id='mw-content-text']")[9][1:]
            self.Spoil = [Item(i,ind,0) for i in self.Spoil]
        except: print ("XEPHYA")
        cursor.execute('INSERT INTO npc (npc_id, npc_name, lvl, link) VALUES (%s,%s,%s,%s)', (ind, self.Name, self.lvl, self.Link))
        cnx.commit()
        ind+=1
        print self.Name









ind=0
driver=webdriver.Chrome("d:/Python27/selenium/webdriver/ChromeDriver")
driver.get("https://l2central.info/classic/%D0%90%D0%B4%D0%B5%D0%BD%D0%B0")
monsters=driver.find_element_by_xpath("//table[@class='quests sortable jquery-tablesorter']").find_element_by_css_selector("tbody").find_elements_by_css_selector("tr")
cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='l2db')
cursor=cnx.cursor()
cursor.execute("TRUNCATE TABLE npc")
cursor.execute("TRUNCATE TABLE loot")
monsters=[monster(i) for i in monsters]
driver.close()