import os
import requests


def upload_image_to_telegraph(image_path):
    url = "https://telegra.ph/upload"
    image_path = f"media/{image_path}"

    with open(image_path, 'rb') as image_file:
        files = {
            'file': ('image.jpg', image_file, 'image/jpeg')
        }

        # POST so'rovini yuborish
        response = requests.post(url, files=files)

        # Natijani qaytarish
        if response.status_code == 200:
            return "https://telegra.ph" + response.json()[0]["src"]
        else:
            return "Failed to upload image"
