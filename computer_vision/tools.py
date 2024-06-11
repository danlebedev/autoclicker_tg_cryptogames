from cv2 import medianBlur, cvtColor, COLOR_BGR2HSV, \
    inRange, COLOR_RGB2BGR
from numpy import array, uint8, where
from numpy.typing import NDArray


def array_index(arr, item, axis):
    return where((arr == item).all(axis=axis))[0][0]


def image_to_array(image):
    return array(image)


def image_to_list(image):
    return array(image).tolist()


def negative_index(arr, index):
    arr_len = len(arr)
    if index >= arr_len or index < 0:
        raise IndexError
    return -arr_len + index


def create_hsv_mask(
        image: NDArray,
        color_min: tuple,
        color_max: tuple,
    ):
    """
    image: image converted to np.array;
    color_min: (r, g, b);
    color_max: (r, g, b);
    return: MathLike.
    """
    # Преобразуем RGB в BGR.
    image = cvtColor(
        src=image,
        code=COLOR_RGB2BGR,
    )
    # Делаем размытие изображения.
    image_blured = medianBlur(
        src=image,
        ksize=19,
    )
    # Конвертируем исходное изображение в цветовую модель HSV.
    hsv_img = cvtColor(
        src=image_blured,
        code=COLOR_BGR2HSV,
    )
    # Подбираем минимальные и максимальные параметры цветового фильтра
    # для выделения объектов.
    hsv_min = array(
        object=color_min,
        dtype=uint8,
    )
    hsv_max = array(
        object=color_max,
        dtype=uint8,
    )
    # Применяем цветовой фильтр к исходному изображению.
    hsv_mask = inRange(
        src=hsv_img,
        lowerb=hsv_min,
        upperb=hsv_max,
    )
    return hsv_mask
