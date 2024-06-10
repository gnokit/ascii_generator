import sys
from PIL import Image
import numpy as np

# Function to convert an image into ASCII art
class ImgToAscii:

    #  ASCII styles for the ASCII art
    ASCII_STYLES = {
        "classic": " .:-=+*%#@",
        "modern": ".,-':;ildxo#",
        "retro": " .,'`^\",:;I@",
        "thick": "@%#*+=-:. ",
        "thin": " ..---===+++***%%%###@@@",
        "simple": "01"
    }

    def __init__(self, style="classic", size=(128,128)): 
        """
        Initialize the ImgToAscii object with a specified style and size.

        Parameters:
        style (str): The ASCII style to be used for generating the art. Default is "classic".
        size (tuple): The size to which the image will be resized (width, height). Default is (128, 128).
        """
        self.style = style
        self.size = size
        self.ascii_chars = self.ASCII_STYLES.get(style, self.ASCII_STYLES["classic"])

    def load_image(self, image_path):
        """
        Load an image from the specified file path.

        Parameters:
        image_path (str): The path to the image file.

        Returns:
        Image: An Image object loaded from the specified file path.
        """
        return Image.open(image_path)

    def generate_ascii_art(self, image):
        """
        Generate ASCII art from the given image.

        Parameters:
        image (Image): The image object to be converted into ASCII art.

        Returns:
        list: A 2D list representing the ASCII art, where each element is a character.
        """
        # Resize the image to the specified size using bicubic resampling
        image = image.resize(self.size, resample=Image.BICUBIC)
        # Convert the image to grayscale
        image = image.convert("L")

        # Convert the grayscale image to a numpy array
        grayscale_image = np.array(image)
        
        # Map each pixel value to an ASCII character based on the specified style
        ascii_art = [
            [self.ascii_chars[int(pixel / 255 * (len(self.ascii_chars) - 1))] for pixel in row]
            for row in grayscale_image
        ]
        return ascii_art

# Check if the script is being run from command line and has two arguments
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python img2ascii.py <image_path> <style>")
        sys.exit(1)

    # Get the image path and style from command line arguments
    image_path = sys.argv[1]
    style = sys.argv[2]

    # Create an instance of ImgToAscii with the specified style
    generator = ImgToAscii(style)

    # Load the image from the file path
    image = generator.load_image(image_path)

    # Generate ASCII art from the image and print it to the console
    ascii_art = generator.generate_ascii_art(image)
    for row in ascii_art:
            print("".join(row))
