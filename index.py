from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv


options = Options()
options.headless = True
options.add_argument("--window-size=1400,1100")
driver = webdriver.Chrome(options=options)

# add url you want to search here starting with https://www
entry = "https://www.google.com/"

o = urlparse(entry)
domain = o.hostname

queue = [entry]
visited = {}

# BFS through site and keep track of visited paths
while len(queue) > 0:

    url = queue.pop(0)

    if url not in visited:

        print(url)

        driver.get(url)

        links = driver.find_elements(By.XPATH, "//a[@href]")

        for link in links:
            href = link.get_attribute('href')
            o = urlparse(href)
            # only add links within the same domain to queue
            if o.hostname == domain:
                queue.append(href)

        visited[url] = True

driver.close()

# write to CSV

f = open('site_paths.csv', 'w')

writer = csv.writer(f)


for key, value in enumerate(visited):
    writer.writerow([value])

f.close()
