import requests
import re
from bs4 import BeautifulSoup

# class Price:
#     def __init__(self,title,price) -> None:
#         self.title=title
#         self.price=price
#     def __str__(self) -> str:
#         return f"{self.title}\t\t{self.price}"

# # -----------------------------------------------------

res=requests.get("https://www.tgju.org/profile/price_dollar_rl")
# # print(res.status_code)
soup=BeautifulSoup(res.content,"html.parser")
# # print(soup)

# # res=soup.find("h1")               #عنوان صفحه
# # print(res)
# # print(res.text)
# # print(res.text.strip())


res=soup.find_all("td",attrs={"class":"text-left"})
my_list=[]
for item in res:
    my_list.append(item)
print(my_list[5])

# 



# my_list=[]
# res=requests.get("https://www.tgju.org/profile/price_dollar_rl")
# soup=BeautifulSoup(res.content,"html.parser")
# res=soup.find_all("td",attrs={"class":"text-left"})
# for p in res:
#     price=p.tr.ins.text.strip()
#     price=re.sub(r",","",price)
#     my_list.append(price)
# print(my_list)


























# url="https://bot.3gh.ir/ex/"

# response=requests.get(url)
# html_content=response.text
# soup=BeautifulSoup(html_content,"html.parser")
# print(soup)
# # price_element=soup.find('span',class_='price')
# # price=price_element.text
# # print(price)