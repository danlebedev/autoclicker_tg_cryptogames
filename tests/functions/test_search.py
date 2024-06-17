from PIL import Image
from computer_vision.cv import search_pixel_in_list, search_pixel_with_getpixel
from computer_vision.tools import image_to_list


src_image = 'tests/3.png'
image = Image.open(src_image)
width = image.width
height = image.height
color_min = (0, 0, 0)
color_max = (0, 0, 0)


def test_search_pixel_list(image, reverse):
    image = image_to_list(image)
    drop_region_coordinates = search_pixel_in_list(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=2,
        step_pixel=5,
        reverse=reverse
    )
    return drop_region_coordinates


def test_search_pixel_with_getpixel(image, reverse):
    drop_region_coordinates = search_pixel_with_getpixel(
        image=image,
        color_min=color_min,
        color_max=color_max,
        step_string=2,
        step_pixel=5,
        reverse=reverse
    )
    return drop_region_coordinates


print(f'reverse: False - {test_search_pixel_list(image, False)}')
print(f'reverse: False - {test_search_pixel_with_getpixel(image, False)}')
print(f'reverse: True - {test_search_pixel_list(image, True)}')
print(f'reverse: True - {test_search_pixel_with_getpixel(image, True)}')
