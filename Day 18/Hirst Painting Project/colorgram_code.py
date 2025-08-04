import colorgram
colors_from_picture = colorgram.extract("20_001.jpg",25)

color_palate = []
for color in colors_from_picture:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    temp_tuple = (r,g,b)
    color_palate.append(temp_tuple)

print(color_palate)

#returns list of the colors in the images

#colors = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

#you can copy this list to the main.py and start working