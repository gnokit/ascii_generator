import sys
from text2img import TextToImage
from img2ascii import ImgToAscii

def generate_ascii_from_text(text):
    """
    Generates ASCII art from a given text.

    Parameters:
    - text (str): The input text to convert into ASCII art.

    Returns:
    - str: The generated ASCII art as a string.
    """

    # Generate an image from the text using TextToImage
    text_to_image = TextToImage()
    image = text_to_image.generate_image(text)    

    # Convert the image to ASCII art using AsciiArtGenerator
    img2ascii = ImgToAscii(style="modern", size=(128, 128))
    return img2ascii.generate_ascii_art(image)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ascii_from_text.py <prompt>")
        sys.exit(1)

    text = sys.argv[1]
    if not text:  # add validation checking on text that must not empty
        print("Error: prompt is empty")
        sys.exit(1)
    
    ascii_art = generate_ascii_from_text(text)
    # Display the text and generated ASCII art
    print(f"Your wish: {text}")
    print(f"Your Artwork")
    for row in ascii_art:
        print("".join(row))
