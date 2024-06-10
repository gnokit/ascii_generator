from diffusers import StableDiffusionPipeline
import torch
import sys
import re
import time
import warnings

class TextToImage:
    """This class is responsible for generating images from text prompts using the stable diffusion model."""

    def __init__(self):
        """Initializes the class and loads the stable diffusion model."""
        # Ignore all warnings
        warnings.filterwarnings("ignore")
        warnings.filterwarnings("ignore", category=FutureWarning)

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  
        """The device on which the model will be run."""
        
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16,
            variant="fp16"
        ).to(self.device)  
        """The stable diffusion model."""

    def generate_image(self, prompt):
        """Generates an image from the given text prompt using the stable diffusion model.

        Args:
            prompt (str): The text prompt to generate an image for.

        Returns:
            PIL.Image: The generated image.
        """
        return self.pipe(prompt).images[0]

    def convert_to_snake_case(self, input_string):
        """Converts a string to snake case by replacing non-alphanumeric characters with underscores and converting the entire string to lowercase.

        Args:
            input_string (str): The input string to be converted.

        Returns:
            str: The input string converted to snake case.
        """
        return re.sub(r'[^a-z0-9]', '_', input_string.lower())

    def get_image_file(self, prompt):
        """Generates a file name for the image using the prompt and the current timestamp.

        Args:
            prompt (str): The text prompt used to generate the image.

        Returns:
            str: The generated file name.
        """
        return f"{self.convert_to_snake_case(prompt)}_{time.time()}.png"

    def run(self):
        """Runs the text-to-image conversion process by checking if a prompt is provided, generating an image using the model, and saving the generated image to a file."""
        if len(sys.argv) != 2:
            print("Usage: python text2img.py <prompt>")
            sys.exit(1)

        prompt = sys.argv[1]
        image = self.generate_image(prompt)
        file_name = self.get_image_file(prompt)
        image.save(file_name)
        print(f"Your Imaginary: {prompt}")
        print(f"Generated: {file_name}")

if __name__ == "__main__":
    text_to_image = TextToImage()
    text_to_image.run()