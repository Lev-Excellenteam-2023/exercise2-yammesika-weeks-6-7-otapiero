from numpy import asarray
from PIL import Image
# define a functioun that get a path to a png file and find the place of the black pixels in each column
# and convert the place number to letters
# and return the letters
def png_deciphering(path):
    image = Image.open(path)
    data = asarray(image)
    list_of_black_pixels_place = []
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] != 255:
                list_of_black_pixels_place.append(j)
                break
    return ''.join([chr(i) for i in list_of_black_pixels_place])








#print(png_deciphering("./ressorces/code.png"))