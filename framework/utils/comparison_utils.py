from PIL import ImageChops, Image

from framework.utils.logger import info


def check_that_images_are_equal(path_to_first_picture, path_to_second_picture):
    info(f"Comparing {path_to_first_picture} with {path_to_second_picture}")
    first_image = Image.open(path_to_first_picture)
    second_image = Image.open(path_to_second_picture)
    return ImageChops.difference(first_image, second_image).getbbox() is None
