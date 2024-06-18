from __future__ import annotations
from cv2 import medianBlur, cvtColor, COLOR_BGR2HSV, \
    inRange, COLOR_RGB2BGR
from cv2.typing import MatLike
from numpy import array, uint8, where
from numpy.typing import NDArray
import os
import shutil
import subprocess
import sys
import tempfile
from PIL import Image


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


def convert_to_hsv_with_blur(image: NDArray) -> MatLike:
    """
    image: image converted to np.array;
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
    return hsv_img


def create_hsv_mask(
    hsv_img: MatLike,
    hsv_min: tuple,
    hsv_max: tuple,
) -> MatLike:
    """
    hsv_min: (h, s, v);
    hsv_max: (h, s, v);
    """
    # Применяем цветовой фильтр к изображению.
    hsv_mask = inRange(
        src=hsv_img,
        lowerb=array(
            object=hsv_min,
            dtype=uint8,
        ),
        upperb=array(
            object=hsv_max,
            dtype=uint8,
        ),
    )
    return hsv_mask


def screenshot_hsv(
    bbox=None,
    include_layered_windows=False,
    all_screens=False,
    xdisplay=None
):
    """Working only on Windows."""
    if xdisplay is None:
        if sys.platform == "darwin":
            fh, filepath = tempfile.mkstemp(".png")
            os.close(fh)
            args = ["screencapture"]
            if bbox:
                left, top, right, bottom = bbox
                args += ["-R", f"{left},{top},{right-left},{bottom-top}"]
            subprocess.call(args + ["-x", filepath])
            im = Image.open(filepath)
            im.load()
            os.unlink(filepath)
            if bbox:
                im_resized = im.resize((right - left, bottom - top))
                im.close()
                return im_resized
            return im
        elif sys.platform == "win32":
            offset, size, data = Image.core.grabscreen_win32(
                include_layered_windows, all_screens
            )
            im = Image.frombytes(
                "HSV",
                size,
                data,
                # RGB, 32-bit line padding, origin lower left corner
                "raw",
                "HSV",
                (size[0] * 3 + 3) & -4,
                -1,
            )
            if bbox:
                x0, y0 = offset
                left, top, right, bottom = bbox
                im = im.crop((left - x0, top - y0, right - x0, bottom - y0))
            return im
    try:
        if not Image.core.HAVE_XCB:
            msg = "Pillow was built without XCB support"
            raise OSError(msg)
        size, data = Image.core.grabscreen_x11(xdisplay)
    except OSError:
        if (
            xdisplay is None
            and sys.platform not in ("darwin", "win32")
            and shutil.which("gnome-screenshot")
        ):
            fh, filepath = tempfile.mkstemp(".png")
            os.close(fh)
            subprocess.call(["gnome-screenshot", "-f", filepath])
            im = Image.open(filepath)
            im.load()
            os.unlink(filepath)
            if bbox:
                im_cropped = im.crop(bbox)
                im.close()
                return im_cropped
            return im
        else:
            raise
    else:
        im = Image.frombytes("RGB", size, data, "raw", "BGRX", size[0] * 4, 1)
        if bbox:
            im = im.crop(bbox)
        return im
