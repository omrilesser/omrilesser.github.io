from PIL import Image
import os

# Input and output folders
input_folder = "papers_thumbnails"
output_folder = "images/thumbnails"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a regular file and has a supported extension
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        input_path = os.path.join(input_folder, filename)

        # Open the image
        with Image.open(input_path) as img:
            # Resize the image to a width of 300 pixels while maintaining aspect ratio
            img.thumbnail((300, img.height))

            # Save the resized image as a JPEG in the output folder
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_filename)
            img.convert("RGB").save(output_path, "JPEG")

        print(f"Resized and saved as JPG: {output_filename}")
    else:
        print(f"Warning: {filename} not a valid file or supported format - skipping")

print("Batch resizing complete.")
