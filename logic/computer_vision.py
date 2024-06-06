from cv2 import medianBlur, cvtColor, COLOR_BGR2HSV, \
    inRange, findContours, RETR_LIST, CHAIN_APPROX_SIMPLE, \
    fitEllipse, COLOR_RGB2BGR
from numpy import array, uint8


def search_objects_by_color(
        image,
        color_min,
        color_max,
    ):
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
            coordinates.append(map(int, ellipse[0]))
    return coordinates
