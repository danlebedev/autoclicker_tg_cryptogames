from PIL import Image
from computer_vision.cv import search_contour_coordinates, \
    search_pixel_in_array, search_pixel_in_list, search_pixel_with_getpixel
from computer_vision.tools import image_to_list, create_hsv_mask, image_to_array
from tests.tools import check_time


src_image = "tests/time/speed.png"
image = Image.open(src_image)
width = image.width
height = image.height
color_min = (102, 200, 0)
color_max = (220, 255, 125)
skip_pixels = (
    (0, 0, 0),
    (28, 117, 50),
    (24, 99, 42),
    (37, 157, 66),
)


def test_search_pixel_list(image):
    image = image_to_list(image)
    drop_region_coordinates = search_pixel_in_list(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=20,
        step_pixel=20,
        reverse=False
    )

def test_search_pixel_array(image):
    image = image_to_array(image)
    drop_region_coordinates = search_pixel_in_array(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=20,
        step_pixel=20,
        reverse=False
    )


def test_blum_script(image):
    width = image.width
    height = image.height
    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = image.getpixel((x, y))

            # Проверка на зеленые бактерии
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                screen_x = x
                screen_y = y


def test_search_pixel_with_getpixel(image):
    drop_region_coordinates = search_pixel_with_getpixel(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=20,
        step_pixel=20,
        reverse=False
    )

def test_search_pixel_with_getpixel_skip(image, skip):
    drop_region_coordinates = search_pixel_with_getpixel(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=20,
        step_pixel=20,
        skip_pixels=skip,
        reverse=False
    )


def test_search_contour(image):
    image = image_to_array(image)
    hsv_mask = create_hsv_mask(
        image,
        color_min=color_min,
        color_max=color_max,
    )
    search_contour_coordinates(hsv_mask)


check_time(test_search_pixel_list, image, iterations=10)
check_time(test_search_pixel_array, image, iterations=10)
check_time(test_blum_script, image, iterations=10)
check_time(test_search_pixel_with_getpixel, image, iterations=10)
check_time(test_search_pixel_with_getpixel_skip, image, skip_pixels, iterations=10)
check_time(test_search_contour, image, iterations=10)
