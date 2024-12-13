from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PIL import ImageOps

# načtení obrázku a uložení do proměnné
image = Image.open("sailfin.jpg")

# rozostření - vyší císlo -> větší rozostření
blurred_1 = image.filter(ImageFilter.BoxBlur(10))
# při zadání dvou parametrů v array se dá nastavit rozostřování na ose x a y zvlášť
blurred_2 = image.filter(ImageFilter.BoxBlur((35, 1)))

# uložení obrázků
blurred_1.save("blurred1.jpg")
blurred_2.save("blurred2.jpg")

# změnení formátu
png = image.convert("RGB")
png.save("converted.png")

# změna velikosti - zadává se hodnota v pixelech v tuple
resized = image.resize((250, 250))
resized.save("resized.jpg")

# oříznutí
original_size = image.size
cropped = image.crop((400, 0, original_size[0]/2, original_size[1]/2))
cropped.save("cropped.jpg")

# kontrast - na vstupu je float od 0 do 1
temp = ImageEnhance.Contrast(image)
contrast = temp.enhance(0.25)
contrast.save("contrast.jpg")

# světlost
temp = ImageEnhance.Brightness(image)
bright = temp.enhance(1.5)
bright.save("bright.jpg")

# monochrome
monochrome = ImageOps.grayscale(image)
monochrome.save("monochrome.jpg")
