# Mission-to-Mars
Module 10

## Purpose of Analysis
This project utilizes web scraping and various tools to extract data from active websites. Chrome Developer Tools are used to identify HTML components associated with target data, and BeautifulSoup and Splinter automate a browser needed to navigate the websites. All of the extracted data was stored in MongoDB. Finally, the a web application (Flask) is used to display the scraped data on a webpage.

## Results
The data extracted comes from multiple websites containing information about Mars. Here is a summary of some of the elements that display on the webpage:

### Scrape New Data Button
A button displays at the top of the webpage which allows for a user to scrape all of the websites containing the mars information which will update on the page after it's clicked.

### Mars News
A title and paragraph of the most recent news post on http://redplanetscience.com displays.

### Featured Image
A section for a featured image which is taked from http://spaceimages-mars.com displays.

### Mars Facts
A table which contains a list of facts displays next to the featured image.

### Hemisphere Data
A section containing four hemisphere images of Mars and their associated names displays at the bottom of the webpage.

Here are screenshots of the final product (of data scraped on 8/28/2022):

![website_1](https://user-images.githubusercontent.com/107309793/187079791-6b94630a-ada0-4f2f-a551-4af2326ee48e.png)
![website_4](https://user-images.githubusercontent.com/107309793/187079891-fe9be7b3-0a4d-44c8-9598-b70f4a549bd0.png)
