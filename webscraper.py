# Import packages.
import requests
from bs4 import BeautifulSoup

# Fetch HTML content.
urls = ['https://www.artofmanliness.com', 'https://www.catholicgentleman.com', 'https://www.thosecatholicmen.com', 'https://thesimplecatholic.blog/']

# Initialize a string to hold the content for the text file.
text_file_content = ""

# Loop through each URL, scrape headlines, and add them to the content string.
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(['h2', 'h3'])
    
    text_file_content += f"Headlines from {url}\n"
    for headline in headlines:
        if headline.a:  # Check if the headline is a hyperlink
            headline_url = url + headline.a['href'] if 'http' not in headline.a['href'] else headline.a['href']
            text_file_content += f"{headline.name}: {headline.text} - {headline_url}\n"
        else:
            text_file_content += f"{headline.name}: {headline.text}\n"
    text_file_content += "\n"

# Save the aggregated headlines into a text file.
with open("aggregated_headlines_with_links.txt", "w") as f:
    f.write(text_file_content)
