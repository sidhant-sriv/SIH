# Site to scrape https://www.india.gov.in/news_lists
# This is a scraper for the above site. It scrapes the site and collects the text of the link and the link itself in a csv file.
# Use beautifulsoup4 to scrape the site.
# Use csv module to write the data to a csv file.
# Use requests module to get the html content of the site.

import requests
from bs4 import BeautifulSoup
import csv
import difflib # to compare the text of the links

# Get the html content of the site
url = "https://www.india.gov.in/news_lists"
response = requests.get(url)
html_content = response.content

# create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')
# collect all the links in the site
def get_links():
    links = soup.find_all('a')
    links = links[71:153]
    print("Text of the links: ")
    for i in range(len(links)):
        print(links[i].text, sep=": ")
    return links

# redo get_links() but convert all links starting with / with the full url
def get_links_full():
    links = soup.find_all('a')
    links = links[71:153]
    for i in range(len(links)):
        if links[i]['href'].startswith('/'):
            links[i]['href'] = 'https://www.india.gov.in' + links[i]['href']
    return links

# Get all urls and text of the links
def get_urls(links):
    urls = []
    for link in links:
        urls.append(link['href'])
    return urls

def get_text(links):
    text = []
    for link in links:
        text.append(link.text)
    return text
print(get_urls(get_links_full())[0], get_text(get_links_full())[0], sep="\t")

# Write the data to a csv file
# csv should have 3 columns:index, text of the link and the link itself
def write_to_csv():
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Text", "Link"])
        for i in range(len(get_urls(get_links_full()))):
            writer.writerow([i, get_text(get_links_full())[i], get_urls(get_links_full())[i]])

def main():
    write_to_csv()
if __name__ == "__main__":
    main()