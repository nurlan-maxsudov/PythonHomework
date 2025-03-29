from PIL import Image
import numpy as np

with Image.open('lesson-14/homework/images/birds.jpg') as img:
    print(img.mode)
    img_arr = np.array(img)
    print(img_arr)

print(img_arr.shape)

def save_img(arr, name, mode):
    img = Image.fromarray(arr, mode)
    img.save(f'lesson-14/homework/images/{name}.jpg')

gray_img_arr = (img_arr[:, :, 0] * 0.299 + img_arr[:, :, 1] * 0.587 + img_arr[:, : , 2] * 0.114).astype(np.uint8)

# save_img(gray_img_arr, 'gray_birds', 'L')

cropped_img = img_arr[100:300, 200:500, ]
save_img(cropped_img, 'cropped_birds', 'RGB')

resized_img = img_arr[::2, ::2, :]
save_img(resized_img, 'resized_birds', 'RGB')

flipped_image_arr = img_arr[::-1, :]
save_img(flipped_image_arr, 'flipped_img', 'RGB')