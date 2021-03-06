import bs4 as bs
import urllib.request
import pickle
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



links = ["https://homeloans.sbi/faq",
         "https://www.sbi.co.in/portal/web/customer-care/faq-car-loan",
         "https://www.sbi.co.in/portal/web/customer-care/faq-educational-loan",
         "https://www.sbi.co.in/portal/web/customer-care/faq-personal-loan",
         "https://www.sbi.co.in/portal/web/customer-care/faq-loan-against-shares-debentures",
         "https://www.sbi.co.in/portal/web/customer-care/faq-festival-loans"]

quest = []
ans = []

for link in links:
    source = urllib.request.urlopen(link).read() #source code

    soup = bs.BeautifulSoup(source,'html.parser') #lxml is the parser,converting source to beautiful soup object

    for div in soup.find_all('div',class_='toggle-div-header'): 
        quest.append(str(div.text))

    for paragraph in soup.find_all('span',class_='bolded-txt'):
       paragraph = paragraph.find_parent('p')    
       ans.append(str(paragraph.text))


file = open('./data/loan_ques','wb')
pickle.dump(quest,file)
file.close()

file = open('./data/loan_ans','wb')
pickle.dump(ans,file)
file.close()

