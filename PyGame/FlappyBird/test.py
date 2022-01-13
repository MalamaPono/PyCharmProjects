import math

# convert function that converts ratio of tutorial sizes to
# my small macbook size. sometimes I use it sometimes I don't
# I usually just test out things and go with what I think looks nice.
def convert(width,height):
    dimensions = (width*2,height*2)
    ratio = (dimensions[0],math.floor((dimensions[1]/1024) * 800))
    return ratio

print(convert(184,267))