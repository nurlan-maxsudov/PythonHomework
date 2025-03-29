import numpy as np

from PIL import Image

def task1():
    F = np.array([32, 68, 100, 212, 77])

    C = (F - 32)*(5/9)

    return C


def task2():
    x = np.array([2, 3, 4, 5])
    y = np.array([1, 2, 3, 4])

    return x**y

def task3():
    A = np.array([[4, 5, 6],
                 [3, -1, 1],
                 [2, 1, -2]])
    
    B = np.array([7, 4, 5])

    solution = np.linalg.solve(A, B)

    return solution

def task4():
    A = np.array([[10, -2, 3],
                  [-2, 8, -1],
                  [3, -1, 6]])
    
    B = np.array([12, -5, 15])

    solution = np.linalg.solve(A, B)

    return solution

with Image.open("lesson-14/homework/images/birds.jpg") as img:
    img_arr = np.array(img)

def save_img(arr, name, mode):
    img = Image.fromarray(arr, mode)
    img.save(f"lesson-14/homework/images/{name}.jpg")

def flip_image():
    flipped_image_arr = img_arr[::-1, :]
    save_img(flipped_image_arr, 'flipped_img', 'RGB')

def add_noise():
    noise = np.random.normal(0, 50, img_arr.shape).astype(np.uint8)

    noisy_img_arr = np.clip(img_arr + noise, 0, 255)

    save_img(noisy_img_arr, 'noisy_img', 'RGB')


def brighten_channels():
    brightened_img_arr = img_arr.copy()
    brightened_img_arr[:, :, 0] = np.clip(img_arr[:, :, 0] + 40, 0, 255).astype(np.uint8)


    save_img(brightened_img_arr, 'brightened_img', 'RGB')

def apply_mask():
    img_arr[100:300, 200:500, :] = 0
    save_img(img_arr, 'masked_img', 'RGB')

apply_mask()
