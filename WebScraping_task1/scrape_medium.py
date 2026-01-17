# Import required libraries
import os
import requests
from bs4 import BeautifulSoup

# ---------------- Code goes here ----------------

# Medium article URL (Archived version)
url = "https://web.archive.org/web/20191126074327/https://medium.com/@subashgandyer/papa-what-is-a-neural-network-c5e5cc427c7"

# Send HTTP request
response = requests.get(url)

# Check response status
if response.status_code != 200:
    print("Error: Unable to fetch the webpage")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract all paragraph tags
paragraphs = soup.find_all("p")

# Store article text
article_text = ""

for para in paragraphs:
    article_text += para.get_text() + "\n"

# Create output directory
folder_name = "scraped_articles"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Define output file path
file_path = os.path.join(folder_name, "medium_article.txt")

# Write extracted text to file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(article_text)

print("Web scraping completed successfully!")
print("Text file saved at:", file_path)

# ---------------- Code ends here ----------------