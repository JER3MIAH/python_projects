from PIL import Image, ImageFilter

img = Image.open('./006 astro.jpg')

# new_img = img.resize(400, 400)
img.thumbnail((400, 200))
img.save('thumbnail.jpg')
