# PIL/ Pillow library

# The Python Imaging Library (PIL) is a popular open-source library used for image processing and manipulation in Python. It provides a wide range of functionalities to handle images, such as opening, saving, modifying, and creating new images. However, it's important to note that PIL has not been actively maintained since 2011, and its fork, Pillow, is the recommended alternative.

# Here are some common usages of the PIL library (or its fork, Pillow) with examples:

# 1. Opening and displaying an image:
   
   from PIL import Image

   image = Image.open("image.jpg")
   image.show()
   

# 2. Resizing an image:
   
   from PIL import Image

   image = Image.open("image.jpg")
   resized_image = image.resize((300, 200))
   resized_image.save("resized_image.jpg")
   

# 3. Rotating an image:
   
   from PIL import Image

   image = Image.open("image.jpg")
   rotated_image = image.rotate(90)
   rotated_image.save("rotated_image.jpg")
   

# 4. Applying image filters:
   
   from PIL import Image, ImageFilter

   image = Image.open("image.jpg")
   blurred_image = image.filter(ImageFilter.BLUR)
   blurred_image.save("blurred_image.jpg")
   

# 5. Adding text to an image:
   
   from PIL import Image, ImageDraw, ImageFont

   image = Image.open("image.jpg")
   draw = ImageDraw.Draw(image)
   font = ImageFont.truetype("arial.ttf", 30)
   draw.text((50, 50), "Hello, PIL!", fill="red", font=font)
   image.save("text_image.jpg")
   

# 6. Image cropping:
   
   from PIL import Image

   image = Image.open("image.jpg")
   cropped_image = image.crop((100, 100, 400, 400))
   cropped_image.save("cropped_image.jpg")
   

# 7. Converting image formats:
   
   from PIL import Image

   image = Image.open("image.png")
   image.save("image.jpg")
   

# These examples demonstrate only a fraction of what PIL/Pillow can do. You can explore the library's documentation to discover more features and functionalities for your specific needs.