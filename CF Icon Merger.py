import PIL.Image


#number needs to be in quotation marks (a string) so that numbers like 0001 can be input
def combineImages(number, color):
	path = "example script/Icons/UnitThumb" + number + ".png"
	borderpath = "example script/Misc/frame" + color + ".png"
	backpath = "example script/Misc/thumbBack.png"

	unitImage = PIL.Image.open(path)
	unitBorder = PIL.Image.open(borderpath)
	unitBack = PIL.Image.open(backpath)

	unitImage.paste(unitBorder, (0,0), unitBorder)
	unitBack.paste(unitImage, (0,0), unitImage)

	unitBack.save(number + ".png")


def rGB(number):
	path = "example script/Icons/UnitThumb" + number + ".png"
	image = PIL.Image.open(path)
	image.convert('RGB')
	image.save(path)

rGB("0784")
combineImages("9076", "Yellow")