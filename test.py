from bs4 import BeautifulSoup

with open("test.html", 'r+') as html_file:
    content = html_file.read()

soup = BeautifulSoup(content , 'lxml')
courses_html_tags = soup.find_all('h5')
for course in courses_html_tags:

    
title = soup.title   
title.string ="hello"


html_file.seek(0) 
html_file.write(str(soup))
