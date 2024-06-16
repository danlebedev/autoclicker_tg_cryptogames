from cv2 import findContours, RETR_LIST, CHAIN_APPROX_SIMPLE, \
    fitEllipse
from .tools import negative_index, array_index
from numpy.typing import NDArray
from pyautogui import locate, ImageNotFoundException, center, screenshot
import time


def search_contour_coordinates(hsv_mask):
    """
    Средняя скорость. Скорость не сильно уменьшается при увеличении разрешения.

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


def search_pixel_in_list(
        image: list,
        color_min: tuple,
        color_max: tuple,
        skip_pixels: tuple = None,
        step_string=1,
        step_pixel=1,
        reverse=False,
    ):
    """
    Низкая скорость. Скорость почти не увеличивается при увеличении значений step_.
    При значениях step_ = 1 имеет наивысшую скорость из всех остальных search_pixel_() функций,
    но медленнее search_contour_coordinates().
    При значениях step_ > 20 медленее search_contour_coordinates().

    image: converted to list image;
    color_min: (r, g, b);
    color_max: (r, g, b);
    skip_pixels: ((r, g, b), (r, g, b) ...)
    step_string: step of selected elements from the array obtained from the image by y axis;
    step_pixel: step of selected elements from the array obtained from the image by x axis;
    reverse: True - search from bottom right to top left;
    return: (x, y) coordinates.
    """
    if reverse:
        step_string = -step_string
        step_pixel = -step_pixel

    image_slice = image[::step_string]
    for string in image_slice:
        string_slice = string[::step_pixel]
        for pixel in string_slice:
            skip = False
            if skip_pixels:
                for skip_pixel in skip_pixels:
                    if (pixel[0] == skip_pixel[0]) and \
                        (pixel[1] == skip_pixel[1]) and \
                        (pixel[2] == skip_pixel[2]):
                        skip = True
                        break

            if not skip:
                if (pixel[0] >= color_min[0] and pixel[0] <= color_max[0]) and \
                    (pixel[1] >= color_min[1] and pixel[1] <= color_max[1]) and \
                    (pixel [2] >= color_min[2] and pixel[2] <= color_max[2]):
                    pixel_index = string_slice.index(pixel) * abs(step_pixel)
                    string_index = image_slice.index(string) * abs(step_string)
                    if reverse:
                        return abs(negative_index(string, pixel_index) + 1), abs(negative_index(image, string_index + 1))
                    return pixel_index, string_index
    else:
        return None


def search_pixel_in_array(
        image: NDArray,
        color_min: tuple,
        color_max: tuple,
        skip_pixels: tuple = None,
        step_string=1,
        step_pixel=1,
        reverse=False,
    ):
    """
    Средняя скорость. Скорость значительно увеличивается при увеличении значений step_.
    При значениях step_ = 1 имеет самую низкую скорость из всех остальных search_pixel_() функций и
    медленнее search_contour_coordinates().
    При значениях step_ > 20 быстрее search_contour_coordinates().

    image: converted to list image;
    color_min: (r, g, b);
    color_max: (r, g, b);
    skip_pixels: ((r, g, b), (r, g, b) ...)
    step_string: step of selected elements from the array obtained from the image by y axis;
    step_pixel: step of selected elements from the array obtained from the image by x axis;
    reverse: True - search from bottom right to top left;
    return: (x, y) coordinates.
    """
    if reverse:
        step_string = -step_string
        step_pixel = -step_pixel

    image_slice = image[::step_string]
    for string in image_slice:
        string_slice = string[::step_pixel]
        for pixel in string_slice:
            skip = False
            if skip_pixels:
                for skip_pixel in skip_pixels:
                    if (pixel[0] == skip_pixel[0]) and \
                        (pixel[1] == skip_pixel[1]) and \
                        (pixel[2] == skip_pixel[2]):
                        skip = True
                        break

            if not skip:
                if (pixel[0] >= color_min[0] and pixel[0] <= color_max[0]) and \
                    (pixel[1] >= color_min[1] and pixel[1] <= color_max[1]) and \
                    (pixel [2] >= color_min[2] and pixel[2] <= color_max[2]):
                    pixel_index = array_index(string_slice, pixel, 1) * abs(step_pixel)
                    string_index = array_index(image_slice, string, 1) * abs(step_string)
                    if reverse:
                        return abs(negative_index(string, pixel_index) + 1), abs(negative_index(image, string_index + 1))
                    return pixel_index, string_index
    else:
        return None


def locateOnScreen(
        template,
        screenshotIm=None,
        minSearchTime=0,
        **kwargs
    ):
    """TODO - rewrite this
    minSearchTime - amount of time in seconds to repeat taking
    screenshots and trying to locate a match.  The default of 0 performs
    a single search.
    """
    start = time.time()
    while True:
        try:
            # the locateAll() function must handle cropping to return accurate coordinates,
            # so don't pass a region here.
            if not screenshotIm:
                screenshotIm = screenshot(region=None)
            retVal = locate(template, screenshotIm, **kwargs)
            try:
                screenshotIm.fp.close()
            except AttributeError:
                # Screenshots on Windows won't have an fp since they came from
                # ImageGrab, not a file. Screenshots on Linux will have fp set
                # to None since the file has been unlinked
                pass
            if retVal or time.time() - start > minSearchTime:
                return retVal
        except ImageNotFoundException:
            if time.time() - start > minSearchTime:
                return None


def locateCenterOnScreen(
        template,
        **kwargs
    ):
    """
    TODO
    """
    coords = locateOnScreen(template, **kwargs)
    if coords is None:
        return None
    else:
        # Don't change, device.click() need float coordinates.
        return tuple(map(float, center(coords)))
