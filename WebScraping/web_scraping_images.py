# this is my personal code that is kind of slow and doesn't work that well. used just for fun.
# All automatic no manual work

from selenium import webdriver
import requests
import io
from PIL import Image
import time
from selenium.webdriver.common.by import By

PATH = '/Users/malamapono/Desktop/chromedriver'

wd = webdriver.Chrome(PATH)

def download_image(download_path,url,file_name):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + file_name

        with open(file_path,'wb') as file:
            image.save(file,'JPEG')
        print('success')

    except Exception as e:
        print('FAILED',e)

def get_google_images(wd,delay,max_images,url):
    def scroll_down(wd):
        wd.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(delay)

    wd.get(url)
    image_urls = set()
    skips = 0
    # once break 5 times, just return the images found even if you didn't reach max_images and stop the infinite loop.
    breaks = 0

    while (len(image_urls) + skips) < max_images:
        scroll_down(wd)
        thumbnails = wd.find_elements(By.CLASS_NAME,'Q4LuWd')

        load_more_button = wd.find_elements(By.CLASS_NAME,"tQj5Y ghyPEc IqBfM ecJEib EWZcud eejsDc uirfo notranslate Wq3Ysf EIlDfe cjGgHb d8Etdd LcUz9d")
        if load_more_button:
            print('Loaded more button')
            wd.execute_script("document.getElementsByClassName('tQj5Y ghyPEc IqBfM ecJEib EWZcud eejsDc uirfo notranslate Wq3Ysf EIlDfe cjGgHb d8Etdd LcUz9d').click();")

        for img in thumbnails[len(image_urls) + skips:max_images]:
            try:
                img.click()
                # time.sleep(delay)
            except:
                continue

            images = wd.find_elements(By.CLASS_NAME,'n3VNCb')
            for image in images:
                if image.get_attribute('src') in image_urls:
                    max_images += 1
                    skips += 1
                    breaks += 1
                    print(breaks,'*************')
                    if breaks == 20:
                        return image_urls
                    else:
                        break

                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))
                    print(len(image_urls))

    return image_urls

search = input('Look something up: ')
url = 'https://www.google.com/search?tbm=isch&q=' + search
images_urls = get_google_images(wd,2,50,url)

for i, url in enumerate(images_urls):
    download_image('images/',url,str(i) + '.jpg')

wd.quit()
