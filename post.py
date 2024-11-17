import os
from atproto import Client, models
from themify import generate_image


def post():
	BLUESKY_USER = os.getenv('BLUESKY_USER')
	BLUESKY_PASS = os.getenv('BLUESKY_PASS')

	client = Client()
	client.login(BLUESKY_USER, BLUESKY_PASS)

	img, attrib_text = generate_image()

	IMAGE_PATH = './post_me.png'
	IMAGE_ALT_TEXT = attrib_text
      
	with open(IMAGE_PATH, 'rb') as f:
		img_data = f.read()	  
		client.send_image(
			text='', image=img_data, image_alt=IMAGE_ALT_TEXT)

if __name__ == '__main__':
    post()





