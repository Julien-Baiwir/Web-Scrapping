from bs4 import BeautifulSoup

with open('test.html','r') as html_file:
     content = html_file.read()
    #  print(content)
     soup = BeautifulSoup(content, 'lxml')
     # print(soup.prettify())
     tags = soup.find('h5')
    #  print(tags)    
     courses_html_tags = soup.find_all('h5')[1]
    #  print(courses_html_tags)  
     for course in courses_html_tags:
         print(course.text)
     title = soup.title
     title.string = "hello"
     print(title.text)
     print(soup)
#      html_file.seek(0)  # Move the file pointer to the beginning
#      html_file.write(str(soup))  # Convert soup to string representation
# Converting the soup object to a string using str(soup) is necessary when saving the modified HTML content back to the original file (test.html) in the provided code. This is because the soup object represents a parsed HTML structure, not a plain text string.
# print("Title changed! Check test.html.")        
     
