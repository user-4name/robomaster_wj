import cv2
import numpy as np
import urllib.request
import os

def download_image(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        print("图片已下载到")
        return True
    except Exception as e:
        print(f"下载图片失败: {e}")
        return False

def calculate_yd(contour):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)    
    if perimeter == 0:
        return 0
        
    yd = 4 * np.pi * area / (perimeter * perimeter)#圆度
    return yd

def locate(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("无法读取图片")
        return
    
    #副本
    result_image = image.copy()
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    a, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, b = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    fit_yd = 0
    best_contour = None
    box = None
    
    for i, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        
        circularity = calculate_yd(contour)
        
        x, y, w, h = cv2.boundingRect(contour)
        
        print(f"轮廓 {i}: 面积={area:.2f}, 圆度={circularity:.3f}, 位置=({x},{y})")
        #更新
        if circularity > fit_yd:
            fit_yd = circularity
            best_contour = contour
            box = (x, y, w, h)
    
    if best_contour is not None:
        print(f"最圆的轮廓， 圆度wei{fit_yd:.3f}")
        x, y, w, h = box
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 255, 0), 2)       
        cv2.drawContours(result_image, [best_contour], -1, (255, 0, 0), 2)        
        print(f"矩形框位置: x={x}, y={y}, width={w}, height={h}")

    else:
        print("未找到圆形轮廓")
        return

    cv2.imshow('Original Image', image)
    cv2.imshow('Binary Image', binary)
    cv2.imshow('Detected Rune', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():

    url = "https://raw.githubusercontent.com/Cygnomatic/Cygnomatic-Site/main/docs/test_rune.png"
    image_path = "test_rune.png"
    download_image(url, image_path)  
    locate(image_path)

if __name__ == "__main__":
    main()