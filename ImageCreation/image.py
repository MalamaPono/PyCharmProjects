from PIL import ImageFont, Image, ImageDraw

def create_credits(patron_names):
    text_y_position = 800
    text_padding = 120
    image_width = 1920
    image_height = (len(patron_names) * text_padding) + (text_y_position * 2)

    img = Image.new('RGB',(image_width,image_height),color=(58,63,68))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('/Users/malamapono/Library/Fonts/Raleway-Italic-VariableFont_wght.ttf',100)
    for name in patron_names:
        text_width, text_height = draw.textsize(name,font=font)
        draw.text( ((image_width-text_width)/2, text_y_position),name,font=font,fill=(250,250,250) )
        text_y_position += text_padding

    img.save('credits.png')

create_credits(['John Balto','Tony Fergy','Joe Toescho','Katherine Cline'])
