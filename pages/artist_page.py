"""Artist CLASSES"""

import os
import certifi

os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import torch
import torch.nn.functional as F
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
import requests
from io import BytesIO


class ArtistPage:
    def __init__(self, driver):
        self.driver = driver
        self.device = torch.device("cpu")
        self.mtcnn = MTCNN(image_size=160, device=self.device)
        self.resnet = InceptionResnetV1(pretrained="vggface2").eval().to(self.device)

        self.urls = []

    def find_artist(self, artist):
        """Function searches for the Artist's Profile"""
        self.driver.find_element(*ArtistLocators.PEOPLE).click()
        popular_people_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ArtistLocators.POPULAR_PEOPLE))
        popular_people_btn.click()
        search_icon = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ArtistLocators.SEARCH_ICON))
        search_icon.click()
        serach_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ArtistLocators.ARTIST_SEARCH))
        serach_field.send_keys(artist + Keys.ENTER)

    def open_artist_gallery(self, artist):
        """Function opens Artist's gallery"""
        art_profile = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ArtistLocators.ART_PROFILE(artist)))
        art_profile.click()

        actions = ActionChains(self.driver)
        media_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ArtistLocators.MEDIA_BTN))
        actions.move_to_element(media_btn).perform()

        media_profile = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(ArtistLocators.MEDIA_PROFILE))
        media_profile.click()

    def collect_images(self):
        """Function returns the collection of Artist's images"""
        images = self.driver.find_elements(*ArtistLocators.PROFILE_IMAGES)
        self.urls = [img.get_attribute("src") for img in images]
        return self.urls

    def compare_images(self, wiki_pictr, urls):
        """Pillow (PIL) – load images from local files or URLs.
        MTCNN – detect and align faces in images.
        InceptionResnetV1 (Facenet-PyTorch) – convert faces into numerical embeddings.
        PyTorch (cosine similarity) – compare embeddings to determine image matches."""
        img1 = Image.open(wiki_pictr)
        emb1 = self.resnet(self.mtcnn(img1).unsqueeze(0))

        results = []
        for img_path_or_url in urls:
            if img_path_or_url.startswith("http"):
                response = requests.get(img_path_or_url, verify=True)
                img2 = Image.open(BytesIO(response.content))
            else:
                img2 = Image.open(img_path_or_url)

            emb2 = self.resnet(self.mtcnn(img2).unsqueeze(0))
            sim = F.cosine_similarity(emb1, emb2).item()
            print(f"{img_path_or_url}: similarity = {sim:.4f}")
            results.append((img_path_or_url, sim))

        return results
