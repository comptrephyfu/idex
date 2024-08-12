from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
image = Image.new('RGB', (300, 200), 'white')
draw = ImageDraw.Draw(image)

# Specify the font and size
font = ImageFont.truetype('arial.ttf', 12)

# Specify the text and its coordinates
text = "Pour attaquer :   ou"
x, y = 30, 70

# Draw the text on the image
draw.text((x, y), text, font=font, fill='black')

# Save the image
image.save('output.png')
