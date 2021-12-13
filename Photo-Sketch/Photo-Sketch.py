import numpy as np
import pandas as pd
import cv2
from tqdm import tqdm
import os
import numpy as np
# ENHANCING THE INTEGRATED IMAGE USING MULTISCALE RETINEX
def singleScaleRetinex(img,variance):
    retinex = np.log10(img) - np.log10(cv2.GaussianBlur(img, (0, 0), variance))
    return retinex

def multiScaleRetinex(img, variance_list):
    retinex = np.zeros_like(img)
    for variance in variance_list:
        retinex += singleScaleRetinex(img, variance)
    retinex = retinex / len(variance_list)
    return retinex

   

def MSR(img, variance_list):
    img = np.float64(img) + 1.0
    img_retinex = multiScaleRetinex(img, variance_list)

    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break            
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break            
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                               (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                               * 255
    img_retinex = np.uint8(img_retinex)        
    return img_retinex



def SSR(img, variance):
    img = np.float64(img) + 1.0
    img_retinex = singleScaleRetinex(img, variance)
    for i in range(img_retinex.shape[2]):
        unique, count = np.unique(np.int32(img_retinex[:, :, i] * 100), return_counts=True)
        for u, c in zip(unique, count):
            if u == 0:
                zero_count = c
                break            
        low_val = unique[0] / 100.0
        high_val = unique[-1] / 100.0
        for u, c in zip(unique, count):
            if u < 0 and c < zero_count * 0.1:
                low_val = u / 100.0
            if u > 0 and c < zero_count * 0.1:
                high_val = u / 100.0
                break            
        img_retinex[:, :, i] = np.maximum(np.minimum(img_retinex[:, :, i], high_val), low_val)
        
        img_retinex[:, :, i] = (img_retinex[:, :, i] - np.min(img_retinex[:, :, i])) / \
                               (np.max(img_retinex[:, :, i]) - np.min(img_retinex[:, :, i])) \
                               * 255
    img_retinex = np.uint8(img_retinex)        
    return img_retinex







path='images/'
os.mkdir("sketches")
for i in tqdm(range(19,61 )):
  p=path + str(i) + ".jpg"
  image = cv2.imread(p)
  height, width, _ = image.shape
  img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
  #BILATERAL FILTERING
  # (a) OBTAINING BASE IMAGE (for large value of σr)
  bigblur = cv2.bilateralFilter(img,6,700,0.02*width)

  # (b) OBTAINING BASE IMAGE (for small value of σr)
  smallblur = cv2.bilateralFilter(img,60,90,0.02*width)

  # TWO SCALE IMAGE DECOMPOSITION
  # DETAILED IMAGE = INPUT IMAGE - BASE IMAGE(generated by bilateral filtering)
  # (1) OBTAINING PROMINENT FACIAL FEATURES
  pff = cv2.add(img, -bigblur)

  # (2) OBTAINING SHADOW DETAILS
  sd = cv2.add(img, -smallblur)

  # INTEGRATING IMAGES (1) AND (2)
  fsd = cv2.addWeighted(sd, 0.5, pff, 0.5, 0)

  variance_list=[15, 80, 30]
  variance=300

  im_msr = MSR(fsd, variance_list)

  im_msr_gray= cv2.cvtColor(im_msr, cv2.COLOR_BGR2GRAY)

  img_gray = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
  #img_gray = cv2.resize(img_gray, (100,1)

  img_gray_inv = 255 - img_gray

  img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
                              sigmaX=0, sigmaY=0)

  def dodgeV2(image, mask):
      return cv2.divide(image, 255-mask, scale=256)

  img_blend = dodgeV2(img_gray, img_blur)
  b = "sketches/" + str(i) +".jpg"

  final_op=cv2.addWeighted(im_msr_gray,0.2,img_blend,0.8,0)
  cv2.imwrite(b, final_op)
         



