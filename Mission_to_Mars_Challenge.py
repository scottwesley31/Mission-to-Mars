#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup (and other dependencies)
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


# Set executable path and set up browser for scraping
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Assign the URL and instruct browser to visit it
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# Set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
slide_elem


# In[5]:


# Find the title information
slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Set up the URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


# Create pandas DataFrame from Mars Facts table at https://galaxyfacts-mars.com
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


# Convert df back into HTML code
df.to_html()


# In[15]:


# Close the browser
browser.quit()


# # Challenge Starter Code

# In[16]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[17]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[18]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[19]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[20]:


slide_elem.find('div', class_='content_title')


# In[21]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[22]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[23]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[24]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# full_image_elem


# In[25]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[26]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[27]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[28]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[29]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[30]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[31]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
# url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)


# In[32]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[33]:


# Scrape for just one image url 
img_item = img_soup.find_all('div', class_='item')[0].find('a')['href']
img_item


# In[34]:


# Scrape for all of the image urls
img_items = img_soup.find_all('div', class_='item')
for img in img_items:
    img_url = img.find('a')['href']
    #browser.find_by_css(string).a.product-item.click() <-- HTML element
    #sample image anchor tag .find_by_text <-- a tag text
    
    print(img_url)


# In[35]:


# List comprehension
[print(img.find('a')['href']) for img in img_items]


# In[36]:


# Use find_by_css to navigate to full-resolution page
div_css = browser.find_by_css('div[class="item"]')[0]
div_css.click()


# In[37]:


# Scrape for just one image title
img_title = img_soup.find_all('div', class_='item')[0].find('h3').text
img_title


# In[38]:


# Scrape for all of the image titles
img_titles = img_soup.find_all('div', class_='item')
for title in img_titles:
    img_title = title.find('h3').text
    print(img_title)


# In[39]:


# Figure out how to navigate to the HTML link to the full-size image and click it

full_image_elem = browser.find_by_css('a.product-item h3')[0]
full_image_elem.click()

# Use index to navigate to each individual page


# In[40]:


# Figure out how to click on the jpeg URL
# full_image_URL = browser.find_by_text('Sample')['href']
# full_image_URL
browser.back()


# In[41]:


# Create a for loop to grab all the full image URLs
for i in range(4):
    full_image_elem = browser.find_by_css('a.product-item h3')[i]
    full_image_elem.click()
    full_image_URL = browser.find_by_text('Sample')['href']
    print(full_image_URL)
    browser.back()


# In[42]:


div_items = img_soup.find_all('div', class_='item')
hemisphere_image_urls = []
for div_item in div_items:
    dict = {}
    img_elem = browser.find_by_css('a.product-item h3')
    img_elem.click()
    img_URL = browser.find_by_text('Sample')['href']
    dict['img_url'] = img_URL
    browser.back()
    dict['title'] = div_item.find('h3').text
    hemisphere_image_urls.append(dict)

hemisphere_image_urls


# In[43]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Retrive the image urls and titles
div_items = img_soup.find_all('div', class_='item')
hemisphere_image_urls = []

for div_item in div_items:
    dict = {}
    img_elem = browser.find_by_css('a.product-item h3')
    img_elem.click()
    img_URL = browser.find_by_text('Sample')['href']
    dict['img_url'] = img_URL
    browser.back()
    title = div_item.find('h3').text
    dict['title'] = title
    hemisphere_image_urls.append(dict)


# In[44]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[45]:


# 5. Quit the browser
browser.quit()

