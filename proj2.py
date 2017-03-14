#proj2.py
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
url = "http://nytimes.com"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
head_title = soup.find_all(class_="story-heading")

print_title = []
for item in head_title:
    if item.a:
        print_title.append(item.a.text.replace("\n", " ").strip())
    else:
        print_title.append(item.contents[0].strip())

for title in print_title[:10]:
    print (title)


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
url2 = "https://www.michigandaily.com/"
html2 = urllib.request.urlopen(url2, context=ctx).read()
soup2 = BeautifulSoup(html2, 'html.parser')
mostread = soup2.find(class_='pane-mostread')
li = mostread('li')
for item in li:
    print (item.text)


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
url3 = 'http://newmantaylor.com/gallery.html'
html3 = urllib.request.urlopen(url3, context=ctx).read()
soup3 = BeautifulSoup(html3, 'html.parser')
img = soup3('img')
for item in img:
    try:
        print (item['alt'])
    except:
        print ("No alternative text provided!")



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
url4 = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'
html4 = urllib.request.urlopen(url4, context=ctx).read()
soup4 = BeautifulSoup(html4, 'html.parser')

# find pager-next, if exist link, go to the page, append to a soup_object list
soup_object = []
soup_object.append(soup4)
flag = True

while flag:
    page_next = soup4.find(class_='pager-next')
    if page_next.a:
        base_url = "https://www.si.umich.edu"
        add_url = page_next.a['href']
        url4 = base_url + add_url
        html4 = urllib.request.urlopen(url4, context=ctx).read()
        soup4 = BeautifulSoup(html4, 'html.parser')
        soup_object.append(soup4)
    else:
        flag = False

# for each soup object, find contact details, goto that page, find email, count
count = 0
for item in soup_object:
    contact = item.find_all(class_='field-name-contact-details')
    for email in contact:
        email_url = base_url + email.a['href']
        email_html = urllib.request.urlopen(email_url, context=ctx).read()
        email_soup = BeautifulSoup(email_html, 'html.parser')
        final_email = email_soup.find(class_="field-name-field-person-email")
        count = count + 1
        print (count, final_email.a.text)
