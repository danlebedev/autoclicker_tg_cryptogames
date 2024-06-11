from tests.tools import check_time
from computer_vision.tools import image_to_array, image_to_list
from PIL import Image


src_image = "screenshots/31-05-2024_13-13-18-792172.png"
image = Image.open(src_image)

def test_image_to_array(image):
    image_to_array(image)


def test_image_to_list(image):
    image_to_list(image)


check_time(test_image_to_array, image, iterations=10)
check_time(test_image_to_list, image, iterations=10)