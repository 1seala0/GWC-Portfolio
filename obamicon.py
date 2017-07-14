from PIL import Image


darkBlue = (0, 51, 76)

red = (217, 26, 33)

lightBlue = (112, 150, 158)

yellow = (252, 227, 166)



my_image = Image.open("horse_picture.jpg")
image_list = my_image.getdata()
image_list = list(image_list)



recolored = []
for tuples in image_list:
    x = tuples[0] + tuples[1] + tuples[2]
    if x < 182:
        recolored.append(darkBlue)
    elif x >= 182 and x < 364:
        recolored.append(red)
    elif x >= 364 and x < 546:
        recolored.append(lightBlue)
    elif x >= 546:
        recolored.append(yellow)




new_image = Image.new("RGB", my_image.size)

new_image.putdata(recolored)

new_image.show()

new_image.save("recolored.jpg", "jpeg")
