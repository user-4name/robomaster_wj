import cv2
import numpy as np
import sys
import urllib.request
import os

def download_image(url, filename):
    urllib.request.urlretrieve(url, filename)
    return filename

def detect_red_armor(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图片")
        return
    
    #the following from AI
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # 设定红色的HSV阈值范围（红色在HSV中有两个范围）
    # 范围1：低红色
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    
    # 范围2：高红色
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    
    # 创建两个掩码
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    
    # 合并两个掩码
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # 显示原始图片和掩码
    cv2.imshow('Original Image', image)
    cv2.imshow('Red Mask', red_mask)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    
    url = "https://raw.githubusercontent.com/Cygnomatic/Cygnomatic-Site/main/docs/test_red_armor.jpg"
    image_path = "test_red_armor.jpg"

    download_image(url, image_path)
    print(f"图片已下载")

    detect_red_armor(image_path)

if __name__ == "__main__":
    main()