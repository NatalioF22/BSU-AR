import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://catalog.bridgew.edu/content.php?catoid=19&navoid=2458"

# Send HTTP request and get response
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find course information
    # Look for course listings - this might need adjustment based on the actual HTML structure
    course_sections = soup.find_all('div', class_='field-items')
    
    for section in course_sections:
        # Look for course titles, descriptions, etc.
        course_info = section.find_all(['h3', 'h4', 'p'])
        for info in course_info:
            print(info.text.strip())
    
    # Try to find links to curriculum or course catalog
    curriculum_links = soup.find_all('a', href=True)
    catalog_links = []
    
    for link in curriculum_links:
        if 'catalog' in link.text.lower() or 'curriculum' in link.text.lower() or 'courses' in link.text.lower():
            catalog_links.append(link['href'])
            print(f"Found related link: {link.text} - {link['href']}")
            
    # If specific course catalog link is found, we can scrape that too
    if catalog_links:
        print("\nFound course catalog links. You can modify this code to scrape those for more details.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")