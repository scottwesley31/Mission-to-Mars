# Import Splinter and BeautifulSoup (and other dependencies)
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

# Define scrape_all function which will initialize a browser, create a data dictionary,
# end the WebDriver, and return the scraped data.

def scrape_all():
    # Initialize headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Set news title and paragraph variables; use mars_news function to pull news_title and news_paragraph
    news_title, news_paragraph = mars_news(browser)
    hemisphere_image_urls = hemisphere_data(browser)

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere_image_urls
        # "hemispheres:"{hemisphere_image_urls}
    }

    # Stop webdriver and return data
    browser.quit()
    return data

# Define a news title and paragraph function
def mars_news(browser):

    # Assign the URL and instruct browser to visit it
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# Featured Images

# Define a featured image function
def featured_image(browser):

    # Set up the URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:

        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# Define the Mars Facts function
def mars_facts():

    # Add try/except handling
    try:
        # Create pandas DataFrame from Mars Facts table at https://galaxyfacts-mars.com
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert df back into HTML code, add bootstrap
    return df.to_html()

# Create a function that will scrape the hemisphere data
def hemisphere_data(browser):
    # Use browser to visit the URL 
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    hemisphere_image_urls = []

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Isolate the section of HTML with hemisphere data
    div_items = img_soup.find_all('div', class_='item')
    hemisphere_image_urls = []

    # Add try/except handling
    try:
        i = 0
        for div_item in div_items:
            dict = {}
            img_elem = browser.find_by_css('a.product-item h3')[i]
            img_elem.click()
            img_URL = browser.find_by_text('Sample')['href']
            dict['img_url'] = img_URL
            browser.back()
            title = div_item.find('h3').text
            dict['title'] = title
            hemisphere_image_urls.append(dict)
            i += 1
        return hemisphere_image_urls
    except:
        return None

# Necessary Flask statement for it to run properly (also in app.py)
if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())