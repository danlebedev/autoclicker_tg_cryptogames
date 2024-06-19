from cv2 import namedWindow, imshow, WINDOW_NORMAL, \
    waitKey, cvtColor, imread, COLOR_BGR2HSV, resizeWindow, \
    inRange, COLOR_BGR2RGB
from computer_vision.tools import create_hsv_mask, create_trackbars, \
    get_trackbar_positions
from os import scandir
from numpy import array, uint8


def create_window_with_trackbars(
    windowName,
    mode='RGB'
):
    namedWindow(winname=windowName)

    names_min = create_trackbars(
        windowName=windowName,
        name_suffix='min',
        mode=mode,
    )
    names_max = create_trackbars(
        windowName=windowName,
        name_suffix='max',
        mode=mode,
    )
    return windowName, names_min, names_max


def listen_trackbars(
    windowName,
    names_min,
    names_max,
):
    trackbars_min = get_trackbar_positions(
        trackbarNames=names_min,
        windowName=windowName,
    )
    trackbars_max = get_trackbar_positions(
        trackbarNames=names_max,
        windowName=windowName,
    )
    return trackbars_min, trackbars_max


def hsv_color_settings(path):
    namedWindow('Origin', WINDOW_NORMAL)
    resizeWindow(
        'Origin',
        width=400,
        height=600,
    )
    namedWindow('Result', WINDOW_NORMAL)
    resizeWindow(
        'Result',
        width=400,
        height=600,
    )
    windowName, names_min, names_max = create_window_with_trackbars(
        'Settings',
        mode='HSV',
    )
    stop = False

    for image_path in scandir(path):
        if stop:
            break

        image = imread(image_path)
        hsv_img = cvtColor(
            image,
            COLOR_BGR2HSV,
        )

        while True:
            hsv_min, hsv_max = listen_trackbars(
                windowName=windowName,
                names_min=names_min,
                names_max=names_max,
            )
            hsv_mask = create_hsv_mask(
                hsv_img=hsv_img,
                hsv_min=hsv_min,
                hsv_max=hsv_max,
            )
            imshow('Origin', image)
            imshow('Result', hsv_mask)
            # Ждем 30 мс, иначе зависают окна.
            key = waitKey(30)

            if key == ord('n'):
                # Next image
                break
            if key == ord('q'):
                stop = True
                break


def rgb_color_settings(path):
    namedWindow('Origin', WINDOW_NORMAL)
    resizeWindow(
        'Origin',
        width=400,
        height=600,
    )
    namedWindow('Result', WINDOW_NORMAL)
    resizeWindow(
        'Result',
        width=400,
        height=600,
    )
    windowName, names_min, names_max = create_window_with_trackbars(
        'Settings',
        mode='RGB',
    )
    stop = False

    for image_path in scandir(path):
        if stop:
            break

        image = imread(image_path)
        rgb_image = cvtColor(
            image,
            COLOR_BGR2RGB,
        )
        while True:
            rgb_min, rgb_max = listen_trackbars(
                windowName=windowName,
                names_min=names_min,
                names_max=names_max,
            )
            rgb_mask = inRange(
                rgb_image,
                lowerb=array(rgb_min, uint8),
                upperb=array(rgb_max, uint8),
            )
            imshow('Origin', image)
            imshow('Result', rgb_mask)
            # Ждем 30 мс, иначе зависают окна.
            key = waitKey(30)

            if key == ord('n'):
                # Next image
                break
            if key == ord('q'):
                stop = True
                break


path = 'screenshots'
#hsv_color_settings(path)
rgb_color_settings(path)
