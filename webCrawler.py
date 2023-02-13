import os
import requests
import bs4

def scraper(search_term, path):
    # set up the URL with the search term
    url =  f"https://unsplash.com/search/photos/{search_term}"
    # send a request to the website and get the response
    res = requests.get(url)
    # parse the response using BeautifulSoup
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # find all image elements
    images = soup.find_all("img")
    # make a directory to store the images, if it doesn't exist
    os.makedirs(path, exist_ok=True)
    # download the images and save them to the directory
    downloaded_images = 0
    for i, image in enumerate(images):
        try:
            image_url = image["src"]
            response = requests.get(image_url)
            with open(f"{path}/{i}.jpg", "wb") as f:
                f.write(response.content)
                downloaded_images += 1
            if downloaded_images >= 1000:
                break
        except:
            continue

if __name__ == "__main__":
    # specify the search term and the directory path
    search_term = input("specify the image type:")
    path = f"D:\myRepo\{search_term}"
    # run the scraper
    scraper(search_term, path)
