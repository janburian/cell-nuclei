import numpy as np
import skimage.io
from matplotlib import pyplot as plt
from pathlib import Path

def get_num_cols_rows(img: np.array, small_image_size_px: int):
    rows = img.shape[0] // small_image_size_px
    cols = img.shape[1] // small_image_size_px

    return (rows, cols)


def divide_image(img: np.array, small_image_size_px):
    orig_image_size = (img.shape[0], img.shape[1])
    (num_rows, num_cols) = get_num_cols_rows(img, small_image_size_px)

    divided_images = []

    for i in range(num_rows):
        for j in range(num_cols):

            new_row_start = i * small_image_size_px
            new_row_end = (i + 1) * small_image_size_px

            new_col_start = j * small_image_size_px
            new_col_end = (j + 1) * small_image_size_px

            small_image = img[new_row_start:new_row_end, new_col_start:new_col_end]
            divided_images.append(small_image)

    return [divided_images, orig_image_size]


def merge_smaller_images(divided_images: list, small_image_size_px, orig_image_size: tuple):
    # merged_image = np.zeros()
    merged_image = np.zeros((orig_image_size[0], orig_image_size[1], 3), dtype="uint8")
    (num_rows, num_cols) = get_num_cols_rows(img, small_image_size_px)

    for i in range(num_rows):
        for j in range(num_cols):
            idx = i * num_cols + j
            merged_image[i * small_image_size_px:(i + 1) * small_image_size_px, j*small_image_size_px:(j + 1)*small_image_size_px] = divided_images[idx]

    return merged_image


if __name__ == "__main__":
    img = skimage.io.imread("J7_5_a.png")
    # img = skimage.io.imread("cells.jpg")
    small_image_size = 200
    [divided_images, orig_image_size] = divide_image(img, small_image_size)
    # for i in range(len(divided_images)):
    #     skimage.io.imsave("./divided_images/div_im" + str(i).zfill(3) + ".jpg", divided_images[i])
    #     plt.show()
    merged_img = merge_smaller_images(divided_images, small_image_size, orig_image_size)
    skimage.io.imshow(merged_img)
    plt.show()
    print()