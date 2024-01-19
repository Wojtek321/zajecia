import matplotlib.pyplot as plt
import numpy as np
import cv2
import copy


img1 = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)
# img1 = img1.astype(np.float32)
img2 = cv2.imread("livingroom.tif", cv2.IMREAD_GRAYSCALE)
# img2 = img2.astype(np.float32)


# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(16, 8)
# ax = axs[0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
# ax = axs[1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_a")
#
# fig, axs = plt.subplots(1, 2)
# fig.set_size_inches(16, 8)
# ax = axs[0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
# ax = axs[1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie1_b")













# def adjust_brightness(img, n):
#     img_copy = copy.deepcopy(img)
#     img_copy += n
#     img_copy[img_copy > 255] = 255
#     img_copy[img_copy < 0] = 0
#     return img_copy
#
#
# img1_rozjasniony = adjust_brightness(img1, 60)
# img2_rozjasniony = adjust_brightness(img2, 60)
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
# ax = axs[0,1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img1_rozjasniony, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif - rozjasniony")
# ax = axs[1,1]; ax.hist(img1_rozjasniony.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - rosjasniony - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_a")
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
# ax = axs[0,1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img2_rozjasniony, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif - rozjasniony")
# ax = axs[1,1]; ax.hist(img2_rozjasniony.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - rosjasniony - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie2_b")





















# def adjust_contrast(img, a):
#     img_copy = copy.deepcopy(img)
#     img_copy = (img_copy - 127.5)*a + 127.5
#     img_copy[img_copy > 255] = 255
#     img_copy[img_copy < 0] = 0
#     return img_copy
#
#
# img1_mniejszy_kontrast = adjust_contrast(img1, 0.3)
# img2_wieszky_kontrast = adjust_contrast(img2, 1.7)
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
# ax = axs[0,1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img1_mniejszy_kontrast, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif - mniejszy kontrast")
# ax = axs[1,1]; ax.hist(img1_mniejszy_kontrast.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - mniejszy kontrast - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie3_a")
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
# ax = axs[0,1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img2_wieszky_kontrast, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif - wiekszy kontrast")
# ax = axs[1,1]; ax.hist(img2_wieszky_kontrast.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - wiekszy kontrast - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie3_b")
























# def binarization(img, border):
#     img_copy = copy.deepcopy(img)
#     img_copy[img_copy > border] = 255
#     img_copy[img_copy <= border] = 0
#     return img_copy
#
#
# img1_zbinaryzowany = binarization(img1, 50)
# img2_zbinaryzowany = binarization(img2, 150)
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
# ax = axs[0,1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img1_zbinaryzowany, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif - binaryzacja")
# ax = axs[1,1]; ax.hist(img1_zbinaryzowany.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - binaryzacja - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie4_a")
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
# ax = axs[0,1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img2_zbinaryzowany, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif - binaryzacja")
# ax = axs[1,1]; ax.hist(img2_zbinaryzowany.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - binaryzacja - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie4_b")













# img1_blurred = cv2.GaussianBlur(img1, (21,21), 0)
# img2_blurred = cv2.GaussianBlur(img2, (21,21), 0)
#
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
# ax = axs[0,1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img1_blurred, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif - rozmycie")
# ax = axs[1,1]; ax.hist(img1_blurred.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - rozmycie - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie5_a")
#
# fig, axs = plt.subplots(2, 2)
# fig.set_size_inches(16, 15)
# ax = axs[0,0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
# ax = axs[0,1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# ax = axs[1,0]; ax.imshow(img2_blurred, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif - binaryzacja")
# ax = axs[1,1]; ax.hist(img2_blurred.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - binaryzacja - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
# fig.set_tight_layout(tight=True)
# plt.savefig("Zadanie5_b")










# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#
#
# img1_sharp = cv2.filter2D(img1, -1, kernel)
# img2_sharp = cv2.filter2D(img2, -1, kernel)
img1_sharp = cv2.Canny(img1, 120, 300)
img2_sharp = cv2.Canny(img2, 120, 300)


fig, axs = plt.subplots(2, 2)
fig.set_size_inches(16, 15)
ax = axs[0,0]; ax.imshow(img1, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif")
ax = axs[0,1]; ax.hist(img1.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
ax = axs[1,0]; ax.imshow(img1_sharp, cmap='grey'); ax.axis('off'); ax.set_title("cameraman.tif - uwypuklenie krawedzi")
ax = axs[1,1]; ax.hist(img1_sharp.ravel(), bins=256, range=(0,256)); ax.set_title("cameraman.tif - uwypuklenie krawedzi - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie5_c")

fig, axs = plt.subplots(2, 2)
fig.set_size_inches(16, 15)
ax = axs[0,0]; ax.imshow(img2, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif")
ax = axs[0,1]; ax.hist(img2.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
ax = axs[1,0]; ax.imshow(img2_sharp, cmap='grey'); ax.axis('off'); ax.set_title("livingroom.tif - uwypuklenie krawedzi")
ax = axs[1,1]; ax.hist(img2_sharp.ravel(), bins=256, range=(0,256)); ax.set_title("livingroom.tif - uwypuklenie krawedzi - hisotgram"); ax.set_xlabel("Wartość piksela"); ax.set_ylabel("Ilość pikseli")
fig.set_tight_layout(tight=True)
plt.savefig("Zadanie5_d")
