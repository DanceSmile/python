'''
PIL：Python Imaging Library
已经是Python平台事实上的图像处理标准库了
'''

# 导入
from PIL import Image, ImageFilter, ImageDraw

# 打开图像获取图像信息
im = Image.open('./avatar.jpg')
w, h = im.size
print('original image size: %sx%s' % (w, h))

# 缩放图像
im.thumbnail((w//2, h//2))
# 保存图像
im.save("thumbnil.jpg", 'jpeg')


im1 = Image.open('./avatar.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('filter.jpg', "jpeg")


# 图形验证码
image = Image.new('RGB', (240, 60), (255, 255, 255))
draw = ImageDraw.Draw(image)
import random
def rnd_color():
    return (random.randint(1,255), random.randint(1,255), random.randint(1,255))

for w in range(240):
    for h in range(60):
        draw.point((w,h), fill=rnd_color())


image.save("code.jpg", "jpeg")

