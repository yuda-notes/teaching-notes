# Web Scraping

## Table of Content
- [HTML](#html)
- [Selenium](#selenium)
- [BeautifulSoup](#beautifulsoup)
- [More Example](#more-examples)
  - [Extract Data from Specific Element](#extract-data-from-specific-element)
  - [Extract Data from Specific Element with Specific Attribute](#extract-data-from-specific-element-with-specific-attributes)
  - [Extract Data from Multiple Pages](#extract-data-from-multiple-pages)
## Definition
- Web Scraping is a process of extracting data from website.
- To extract data from website, we must know how to identify HTML components.

## Setup
- Install BeautifulSoup and Selenium
  ```sh
  pip install bs4 selenium
  ```

## HTML
- HTML is the standard markup language for creating Web pages.
- HTML consists of a series of elements that tell the browser how to display the content.
- An HTML element is defined by a start tag, some content, and an end tag.
  ```html
  <tag>content...</tag>
  ```
- Additionally, all HTML elements can have attributes which provide additional information about the elements.
- Attributes are always specified in the start tag in key-value format, e.g. `"name": "john doe"`.
  ```html
  <!-- this is an example of `a` element who has `href` attribute to specifies a link/URL to another page/website -->
  <a href="https://www.w3schools.com">Visit W3Schools</a>
  ```

## Selenium
- Only compatible with: **Chrome**, **Safari**, **Firefox**, and **Edge**
- Initialize browser instance
  ```py
  # import package
  from selenium import webdriver

  # for Chrome
  driver = webdriver.Chrome()
  
  # for Safari
  driver = webdriver.Safari()
  
  # for Firefox
  driver = webdriver.Firefox()
  
  # for Edge
  driver = webdriver.Edge()
  ```
- For **Safari**, you must enable Remote Automation feature before start using Selenium.
  1. Go to Safari > Settings.
  2. Select `Advanced` tab.
  3. Enable "Show features for web developers" option.
  4. Select `Developer` tab.
  5. Enable "Allow remote automation" option.
  6. Done.
- _Optionally_, if you need to specify webdriver for selenium, you can download the driver for each browser
  - [Chrome - ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)
  - [Firefox - GeckoDriver](https://github.com/mozilla/geckodriver/releases)
  - [Edge - MSEdge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads)
  - After downloading and extracting the driver, you can do the initiaton process like this
    ```py
    driver = webdriver.Chrome("path/to/your/driver")
    ```
  
## BeautifulSoup
- BeautifulSoup is a Python library for pulling data out of HTML and XML files.
- Example of scraping process using BeautifulSoup and Selenium.
  ```py
  # import packages
  from bs4 import BeautifulSoup
  from selenium import webdriver

  # initiate browser instance
  driver = webdriver.Chrome()

  # open website URL
  url = "https://www.scrapethissite.com/pages/forms/"
  driver.get(url)

  # extract HTML data from page
  html = driver.page_source

  # parse HTML data to `BeautifulSoup` object
  soup = BeautifulSoup(html, "html.parser")

  # print
  print(soup.prettify())
  ```
- In `BeautifulSoup` object, there are 2 methods that we can use to help us extracting data, `find()` and `find_all()`.
  - `find()` is used to find one element.
    > If the elements have many occurences, then it will only get the first occurence.
  - `find_all()` is used to find elements in many occurences.

## More Examples
### Extract Data from Specific Element
<img width="1440" alt="image" src="https://github.com/user-attachments/assets/f25ddb28-6584-49f2-83e3-adbcc13a6856" />

```py
# import packages
from bs4 import BeautifulSoup
from selenium import webdriver

# initiate browser instance
driver = webdriver.Chrome()

# open website URL
url = "https://www.scrapethissite.com/pages/forms/"
driver.get(url)

# extract HTML data from page
html = driver.page_source

# parse HTML data to `BeautifulSoup` object
soup = BeautifulSoup(html, "html.parser")

# use find() or find_all()
result = soup.find("td")
print("using find(): ", result)

results = soup.find_all("td")
print("using find_all(): ", results)

# optional, to force close the browser instance
driver.close()
```
- Output

  <img width="400" alt="image" src="https://github.com/user-attachments/assets/650a7a94-d698-433f-a284-52ac96901bca" />

  > As we can see, `find()` will always return 1 element/object, while `find_all()` will always return a list of objects.

#### Extract Text/Content from Element
- To extract the content of the element, we can use `get_text()` method.
- But before we can call `get_text()` we must ensure that our element is exists by checking if `element != None` is `True`
- Additionally we can add `strip()` method after extracting content with `get_text()`. This is to trim whitespaces from the text/content
  ```py
  # extracting content and strip whitespaces
  element.get_text().strip()
  ```
### Extract Data from Specific Element with Specific Attribute(s)
```py
# import packages
from bs4 import BeautifulSoup
from selenium import webdriver

# initiate browser instance
driver = webdriver.Chrome()

# open website URL
url = "https://www.scrapethissite.com/pages/forms/"
driver.get(url)

# extract HTML data from page
html = driver.page_source

# parse HTML data to `BeautifulSoup` object
soup = BeautifulSoup(html, "html.parser")

# find elements of `td` with an attribute of `class` with value "name"
results = soup.find_all("td", {"class": "name"})
print("using find_all(): ", results)

# optional, to force close the browser instance
driver.close()
```
- Output

  <img width="556" alt="image" src="https://github.com/user-attachments/assets/14997689-2df6-4698-a7f9-f12da7d3fb82" />

### Extract Data from Multiple Pages
- To extract data from multiple pages, first we need to understand how our browsers work when we are navigating to other pages.
- In some cases, when we click specific page number usually it will redirect to that page.
  <img width="1309" alt="Screenshot 2025-04-14 at 11 56 40" src="https://github.com/user-attachments/assets/b6a9bbb5-2a1a-4245-9a42-dd3e408c8336" />
- And if we look again in the URL bar, we notice some changes our URL.
  <img width="1440" alt="Screenshot 2025-04-14 at 11 59 16" src="https://github.com/user-attachments/assets/eca2e228-13c2-4bc8-bd2a-1e25017f59e4" />
- The additional `page_num=2` in our URL indicate that we are now in the 2nd page. So, if we want to go to another page, we just need to increment/decrement the value.
```py
# import packages
from bs4 import BeautifulSoup
from selenium import webdriver

# initiate browser instance
driver = webdriver.Chrome()

# because we want to get data from multiple pages, we might want to set a global variable as list to store all the data
# we can also use Pandas' DataFrame to store our data
names = []

# we can use loop mechanism to automate multiple page scraping
# for example, we are using this to loop through page 1 to 5 in our website
for number in range(1, 6):
  # open website URL with specific page number
  url = "https://www.scrapethissite.com/pages/forms/?page_num=" + str(number)
  driver.get(url)
  
  # extract HTML data from page
  html = driver.page_source
  
  # parse HTML data to `BeautifulSoup` object
  soup = BeautifulSoup(html, "html.parser")
  
  # find elements of `td` with an attribute of `class` with value "name"
  results = soup.find_all("td", {"class": "name"})

  # because the results is consists of many elements we can use loop to iterate through each element
  for element in results:
    # now in each element we first need to check if the element is exists
    if element != None:
        # extract the content and add to `names` list
        names.append(element.get_text().strip())
    else:
        # add `None` to the list
        names.append(None)

# optional, to force close the browser instance
driver.close()
```
