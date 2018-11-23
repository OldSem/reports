# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import msvcrt


class farm:
    def __init__(self,Info):
        self.Id=Info.get_attribute("class")[Info.get_attribute("class").find("rf"):Info.get_attribute("class").find(" level")]
        self.Level = int(Info.get_attribute("class")[
                  Info.get_attribute("class").find(" level")+6:])
        print (self.Id,self.Level)



class village:
    def __init__(self,Info):
        self.Name=Info.find_elements_by_css_selector("td")[1].text
        self.link=Info.find_elements_by_css_selector("td")[1].find_element_by_css_selector("a").get_attribute("href")
        self.Id=self.link[self.link.find("newdid=")+7:self.link.find("&id=")]
        self.X=Info.find_elements_by_css_selector("td")[2].find_element_by_class_name("cox").text[1:]
        self.Y = Info.find_elements_by_css_selector("td")[2].find_element_by_class_name("coy").text[:-1]
    def bildings(self):
        driver.get(self.link)
        self.farms=driver.find_element_by_id("village_map").find_elements_by_css_selector("img")
        self.farms.pop()
        #print self.farms[0].get_attribute("class")
        self.farms=[farm(i) for i in self.farms]
def upgrade(VilID,FarmId):
    driver.get("http://tclassic.esy.es/TravianZ-master/dorf1.php?newdid="+VilID+"&id=")
    driver.get("http://tclassic.esy.es/TravianZ-master/build.php?id="+FarmId[2:])
    try:driver.find_element_by_partial_link_text("Upgrade to level").click()
    except:
        print("Идет улучшение")
        driver.get("http://tclassic.esy.es/TravianZ-master/dorf1.php")
        return "blyat"
    print(VilID,FarmId)

def ul():
    ulist=[[0,0,100]]
    villages = driver.find_element_by_id("vlist").find_element_by_css_selector("tbody").find_elements_by_css_selector(
        "tr")
    villages = [village(i) for i in villages]
    for i in villages:
        i.bildings()
    for i in villages:
        for j in i.farms:
            if j.Level < ulist[0][2]:
                ulist=[[i.Id,j.Id,j.Level]]
            else:
                if j.Level==ulist[0][2]:
                    ulist.append([i.Id, j.Id, j.Level])
    return ulist


Login = raw_input("Ваш логин ")
Password = raw_input("Ваш пароль ")
driver=webdriver.Firefox()
driver.get("http://tclassic.esy.es/TravianZ-master/dorf1.php")
driver.find_element_by_name("user").clear()
driver.find_element_by_name("user").send_keys(Login)
driver.find_element_by_name("pw").clear()
driver.find_element_by_name("pw").send_keys(Password)
driver.find_element_by_id("btn_login").click()

ulist=ul()
while not(msvcrt.kbhit()):
    print(ulist)
    while ulist != []:
        rezult=upgrade(ulist[0][0],ulist[0][1])
        if rezult!="blyat":ulist.pop(0)
        time.sleep(60)
    ulist=ul()

    print ("process run")

else:
    print ("process stop")



