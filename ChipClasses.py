from pictures import chipsPictures

class Chip:

    value = ''
    img = ''

    def __init__(self, value, img):
        self.value = value
        self.img = img

class Chips:
    chip100 = Chip(100, chipsPictures.blackChip)
    chip25 = Chip(25, chipsPictures.purpleChip)
    chip10 = Chip(10, chipsPictures.blueChip)
    chip5 = Chip(5, chipsPictures.greenChip)
    chip1 = Chip(1, chipsPictures.yellowChip)
    chip0point1 = Chip(0.1, chipsPictures.redChip)