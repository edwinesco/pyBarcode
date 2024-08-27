import barcode
from barcode.writer import ImageWriter
import matplotlib.pyplot as plt
from PIL import Image as PILImage

barcode_format = barcode.get_barcode_class('ean13')

barcode_number = "123123123123"

barcode_image = barcode_format(barcode_number, writer=ImageWriter())

barcode_filename = "barcode_image"
barcode_image.save(barcode_filename)

# Cargamos la imagen
img = PILImage.open(f'{barcode_filename}.png')

# Mostramos la imagen con matplotlib
plt.imshow(img)
plt.axis('off')  # Ocultamos los ejes
plt.show()


