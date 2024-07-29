# @time     ：2024/7/26 15:17
# @author   : 莉光哈哈哈
# @file     : test11_restore_old_photos.py
# @software : PyCharm
'''
使用PIL、Matplotlib、Numpy对模糊老照片进行修复
'''
'''
1、加载图片并将其转换为灰度图
2、对图片进行去噪处理，使用简单的加权平均算法
3、对图片进行锐化处理，使用Unsharp Mask算法，可以帮助突出图片中的细节
4、显示原始图片和修复后的图片
'''
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


# 读取图片并转化为灰度图
def load_image(image_path):
    img = Image.open(image_path)
    return img.convert("L")


# 对图片进行去噪处理
def denoise_image(image, weight=0.1):
    img_array = np.asarray(image, dtype=np.float32)
    out_array = img_array.copy()
    out_array[1:-1, 1:-1] = img_array[1:-1, 1:-1] * (1 - 4 * weight) + (
                img_array[:-2, 1:-1] + img_array[2:, 1:-1] + img_array[1:-1, :-2] + img_array[1:-1, 2:]) * weight
    return Image.fromarray(np.uint8(out_array), "L")


# 对图片进行锐化处理
def sharpen_image(image, radius=2, percent=150):
    return image.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=3))


# 显示图片
def display_image(image):
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.show()


# 主程序
def main():
    image_path = "path/to/your/image.jpg"  # 替换为你的图片路径

    # 加载图片
    image = load_image(image_path)

    # 对图片进行去噪处理
    denoised_image = denoise_image(image)

    # 对图片进行锐化处理
    sharpened_image = sharpen_image(denoised_image)

    # 显示原始图片
    print("原始图片：")
    display_image(image)

    # 显示修复后的图片
    print("修复后的图片：")
    display_image(sharpened_image)


if __name__ == '__main__':
    main()
