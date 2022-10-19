from rembg import remove
from PIL import Image

image_path = 'Image Name' ## ---> Change to Image name

output_image = 'New name of your image' ## ---> Change to new name your image

input = Image.open(image_path)

output = remove(input)

output.save(output_image)