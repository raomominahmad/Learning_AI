import sys
from PIL import Image

images = []

# Define the directory where the images are located
image_dir = "/home/momin/Documents/CS50P/Lecture6/data/"

# Slice everything after the file name (take command line arguments for files)
for arg in sys.argv[1:]:
    image_path = f"{image_dir}{arg}"  # Construct full path for each image
    image = Image.open(image_path)
    images.append(image)

# Save images as a GIF in the same directory
images[0].save(
    f"{image_dir}costumes.gif",  # Full path for saving
    save_all=True,
    append_images=images[1:],  # Append remaining images
    duration=200,
    loop=0
)
