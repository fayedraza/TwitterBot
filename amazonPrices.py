#Created by Fayed Raza


#list of imports
import requests
import sys
from bs4 import BeautifulSoup as soup
import tweepy
import datetime
import sys
import time
from requests_html import HTMLSession
from random import random
from urllib.request import urlopen




class prices:

     #this method is used to get the price 
    def getPrice(self,url):
        urlToScrape = url
        headers = {
        'authority': urlToScrape,
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        session = HTMLSession()
        resp = session.get(urlToScrape)
        resp.html.render()

        priceReadyToScrape = soup(resp.html.html,features="lxml")

        try:
            priceOfproduct = priceReadyToScrape.find('span', id='priceblock_saleprice')  #first we check if a price exists with that tag

            return priceOfproduct.text
        except:
            try:
                priceOfproduct = priceReadyToScrape.find('tr', id='priceblock_dealprice_row') #second we check if a price exists with that tag

                return priceOfproduct.span.text
            except:
                priceOfproduct = priceReadyToScrape.find('td', class_='a-span12')  #final choice to check if a price exists with that tag

                return priceOfproduct.span.text

   #this method is used to get the category 
    def getCategory(self,url):
        urlToScrape = url
        headers = {
        'authority': urlToScrape,
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        session = HTMLSession()
        resp = session.get(urlToScrape)
        resp.html.render()

        productDealsReadyToScrape = soup(resp.html.html,features="lxml")
        try:
            categories = productDealsReadyToScrape.findAll('a', class_='a-link-normal a-color-tertiary')
            return categories[0].text #first choice to get the category
        except:
            categories = productDealsReadyToScrape.findAll('a', class_='a-link-normal')
            return categories[0].text #final choice to get the category

    #this method is used to get the rating 
    def getRating(self,url):
        urlToScrape = url
        headers = {
        'authority': urlToScrape,
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        session = HTMLSession()
        resp = session.get(urlToScrape)
        resp.html.render()

        productDealsReadyToScrape = soup(resp.html.html,features="lxml")


        try:
            rating = productDealsReadyToScrape.find('i', class_='a-icon a-icon-star a-star-4')  #first we check if it is a full 4 star rating
            return rating.span.text
        except:
            try:
                rating = productDealsReadyToScrape.find('i', class_='a-icon a-icon-star a-star-4-5') #first we check if it is between 4 to 5 star rating
                return rating.span.text
            except:
                try:
                    rating = productDealsReadyToScrape.find('i', class_='a-icon a-icon-star a-star-5') #first we check if it is a full 5 star rating
                    return rating.span.text
                except:
                    rating = productDealsReadyToScrape.find('span', class_='a-icon-alt') #final choice
                    return rating.text

 #this method is used to get the title of the product that is on sale 
    def getTitleOfDeal(self,url):
        urlToScrape = url
        headers = {
        'authority': urlToScrape,
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }

        session = HTMLSession()
        resp = session.get(urlToScrape)
        resp.html.render()

        productDealsReadyToScrape = soup(resp.html.html,features="lxml")


        try:
            titleOfDeal = productDealsReadyToScrape.find('span', class_='a-size-large product-title-word-break')  #first tag to get the title
            return titleOfDeal.text
        except:
            titleOfDeal = productDealsReadyToScrape.find('span', class_='a-icon a-icon-star a-star-4-5') #final choice
            return titleOfDeal.text

api = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)


#true/false variables, representing each category
Electronics = True
SportsOutdoors = True
ClothingShoesJewelry = True
AmazonDevices = True
HomeKitchen = True
BeautyPersonalCare = True
CellPhonesAndAcessories = True
ToysGames = True

count = 0 #set count, the number of tweets


#go through the pages
for num in range(1,21):

     #page to scrape
    urlToScrape = 'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-5_4e18_page_'+str(num)+'?gb_f_deals1=dealTypes:DEAL_OF_THE_DAY%252CBEST_DEAL%252CLIGHTNING_DEAL,page:2,sortOrder:BY_SCORE,dealStates:AVAILABLE%252CWAITLIST%252CWAITLISTFULL%252CEXPIRED%252CSOLDOUT%252CUPCOMING,includedAccessTypes:GIVEAWAY_DEAL,dealsPerPage:48&pf_rd_p=4a0dd3f9-e36f-4203-83e5-3cbb64324e18&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=313JNDGF723XPC3PDJYJ&ie=UTF8'         
    
    headers = {
        'authority': urlToScrape,
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }


    session = HTMLSession()
    resp = session.get(urlToScrape)
    resp.html.render()

    productDealsReadyToScrape = soup(resp.html.html,features="lxml")

    productObject = prices()
    listOfProducts =  productDealsReadyToScrape.findAll("a",id="dealTitle")

    #go through the products of each page
    for product in listOfProducts:

        category = ""

        if count == 7:  #once we tweeted 6 products we can end the program for the day
            sys.exit()

        if num < 18: # if page is before 18 we will check the specific category 
            
            try:
                linkOfProduct = product["href"].strip() #get the link
                category = productObject.getCategory(linkOfProduct).strip() #get the category
                print(category)
            except:
                continue
        
            try:
      
                """We will check the category of each product and once we find our match we will mark its boolean variable as false since we will not tweet from that category during that run.
                 If the boolean var is false or the category does not belong with one of them then we will move on to the next product."""

                if  Electronics and (category == 'Electronics' or category == 'Video Games'):
                    AmazonDevices = False
                    Electronics = False
                    count+=2
                elif AmazonDevices and (category == 'Amazon Device' or 'Alexa' in category or 'Amazon' in category):
                    AmazonDevices = False
                    Electronics = False
                    count+=2
                elif ClothingShoesJewelry and category == 'Clothing, Shoes & Jewelry':
                    ClothingShoesJewelry = False
                    count+=1
                elif HomeKitchen and (category == 'Home & Kitchen' or category == 'Tools & Home Improvement' or category == 'Health & Household' or category == 'Patio, Lawn & Garden'):
                    HomeKitchen = False
                    count+=1
                elif CellPhonesAndAcessories and category == 'Cell Phones & Accessories':
                    CellPhonesAndAcessories = False
                    count+=1
                elif BeautyPersonalCare and (category == 'Beauty & Personal Care' or category == 'Pet Supplies'):
                    BeautyPersonalCare = False
                    count+=1
                elif ToysGames and (category == 'Toys & Games' or category == 'Video Games' or category == 'Office Products'):
                    ToysGames = False
                    count+=1
                else:
                    continue
            except:
                continue
        else:
  

            """In the case we are over page 18 we just select one of the true variables fand turn it to false and tweet that product and increase the count"""

            if  Electronics:
                    AmazonDevices = False
                    Electronics = False
                    count+=2
            elif AmazonDevices:
                    AmazonDevices = False
                    Electronics = False
                    count+=2
            elif ClothingShoesJewelry:
                    ClothingShoesJewelry = False
                    count+=1
            elif HomeKitchen:
                    HomeKitchen = False
                    count+=1
            elif CellPhonesAndAcessories:
                    CellPhonesAndAcessories = False
                    count+=1
            elif BeautyPersonalCare:
                    BeautyPersonalCare = False
                    count+=1
            elif ToysGames:
                    ToysGames = False
                    count+=1

        try:

            # used to check if the boolean variables has been decalared
            productNameBoolean = False
            linkOfProductBoolean = True
            priceOfProductBoolean = False
            ratingOfProductBoolean = False
            categoryOfProductBoolean = False

               
            productName = product.span.text.strip()  #get the name of the product
            productNameBoolean = True
            time.sleep(360)
            priceOfProduct = productObject.getPrice(linkOfProduct).strip() #get the price of the product
            priceOfProductBoolean = True
            time.sleep(360)
            ratingOfProduct = productObject.getRating(linkOfProduct).strip() #get the rating of the product
            ratingOfProductBoolean = True

            #tweets the deal
            api.update_status("Product Title: " + productName + "\n" +  "\n" +
              "Price: " + priceOfProduct + "\n" +  "\n" +
              "Rating: " + ratingOfProduct + "\n" +  "\n" +
               "Link: " + linkOfProduct + "\n" +  "\n" + "\n" +  "\n" + "#AmazonDeals" + "  #Amazon"+ "  #DailyDeals" + "  #DealOfTheDay" + " #Deals")
      
        except:
 
                #in the case we get an error we will make the category variable that was turned to false to be true and decrease the count

                if (category == 'Electronics' or category == 'Video Games'):
                    AmazonDevices = True
                    Electronics = True
                    count-=2
                elif category == 'Amazon Device' or 'Alexa' in category or 'Amazon' in category:
                    AmazonDevices = True
                    Electronics = True
                    count-=2
                elif category == 'Clothing, Shoes & Jewelry':
                    ClothingShoesJewelry = True
                    count-=1
                elif category == 'Home & Kitchen' or category == 'Tools & Home Improvement' or category == 'Health & Household' or category == 'Patio, Lawn & Garden':
                    HomeKitchen = True
                    count-=1
                elif category == 'Cell Phones & Accessories':
                    CellPhonesAndAcessories = True
                    count-=1
                elif (category == 'Beauty & Personal Care' or category == 'Pet Supplies'):
                    BeautyPersonalCare = True
                    count-=1
                elif category == 'Toys & Games' or category == 'Video Games' or category == 'Office Products':
                    ToysGames = True
                    count-=1

        time.sleep(500)  #we will rest then 500 seconds later we will go on to the next product
             

        
