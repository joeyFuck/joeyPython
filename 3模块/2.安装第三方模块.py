from PIL import Image
im = Image.open('../resource/image/1.jpg')
print(im.format,im.size,im.mode)

im.thumbnail((100,100))
im.save('../resource/image/thumb.jpg','JPEG')

import  sys
print(sys.path)









