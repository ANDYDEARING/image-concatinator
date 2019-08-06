import sys
from PIL import Image

# write in images to be concatinated
images = ['Walk_000 copy.png', 'Walk_001 copy.png']

# hard code image width and height
width = 1610
height = 1446

new_image = Image.new('RGBA', (width * len(list(images)), height))

corner = 0

for image in images:
    sub_image = Image.open(image)
    new_image.paste(sub_image.copy(),(corner, 0))
    corner += width

new_image.show()
new_image.save('result.png')
# new_image.show()

# widths, heights = zip(*(i.size for i in images))

# total_width = sum(widths)
# max_height = max(heights)

# new_im = Image.new('RGB', (total_width, max_height))

# x_offset = 0
# for im in images:
#   new_im.paste(im, (x_offset,0))
#   x_offset += im.size[0]

# new_im.save('test.jpg')