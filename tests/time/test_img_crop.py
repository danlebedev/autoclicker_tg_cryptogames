from PIL import Image
from tests.tools import check_time


src_image = "tests/time/speed.png"
image = Image.open(src_image)

check_time(image.crop, (20, 20, 500, 500), iterations=100)