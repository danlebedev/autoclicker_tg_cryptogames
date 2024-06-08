from cv2 import medianBlur, cvtColor, COLOR_BGR2HSV, \
    inRange, findContours, RETR_LIST, CHAIN_APPROX_SIMPLE, \
    fitEllipse, COLOR_RGB2BGR
from numpy import array, uint8


def apply_hsv_mask(
        image,
        color_min: tuple,
        color_max: tuple,
    ):
    """
    image: PIL.Image;
    color_min: (r, g, b);
    color_max: (r, g, b);
    return: MathLike.
    """
    # Преобразуем RGB в BGR.
    image = cvtColor(
        src=array(image),
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


def search_contour_coordinates(hsv_mask):
    """
    return: [((x=координата центра, y=координата центра), (a=большая полуось, b=малая полуось), t=угол врщения), ...]
    """
    # Ищем контуры и записываем их в переменную.
    contours, hierarchy = findContours(
        image=hsv_mask,
        mode=RETR_LIST,
        method=CHAIN_APPROX_SIMPLE,
    )

    # Будем сохранять в список найденные координаты эллипсов.
    coordinates = []
    # Перебираем первые 5 контуров в цикле.
    for contour in contours:
        # Выбираем контуры с длиной больше 20 точек.
        if len(contour) > 20:
            # Записываем контур в форме эллипса.
            # fitEllipse возвращает кортеж:
            # ((x=координата центра, y=координата центра), (a=большая полуось, b=малая полуось), t=угол врщения)
            ellipse = fitEllipse(contour)
            # Получаем координаты центра эллипса, приводя их к целому числу.
            coordinates.append(ellipse)
    return coordinates


def search_pixel(
        image,
        color_min: tuple,
        color_max: tuple,
        step_string=1,
        step_pixel=1,
    ):
    """
    image: PIL.Image;
    color_min: (r, g, b);
    color_max: (r, g, b);
    step_string: step of selected elements from the array obtained from the image by y axis;
    step_pixel: step of selected elements from the array obtained from the image by x axis;
    return: (x, y) coordinates.
    """
    image_array = array(image)
    # TODO: избавиться от преобразования в list и перебирать np.array.
    image_list = image_array.tolist()

    image_slice = image_list[::step_string]
    for string in image_slice:
        string_slice = string[::step_pixel]
        for pixel in string_slice:
            if (pixel[0] >= color_min[0] and pixel[0] <= color_max[0]) and \
                (pixel[1] >= color_min[1] and pixel[1] <= color_max[1]) and \
                (pixel [2] >= color_min[2] and pixel[2] <= color_max[2]):
                return (string_slice.index(pixel) * step_pixel, image_slice.index(string) * step_string)
    else:
        return None
