#Need this for basic image processing
import PIL.Image
#Config file, edit that to set parameters to be used here
import IMConfig



#number needs to be in quotation marks (a string) so that numbers like 0001 can be input
def combineImages(number, option1, option2):

	#Path to the main image
	path = IMConfig.mainPath + IMConfig.text + number + ".png"
	#Path to the border image
	borderpath = IMConfig.borderPath + IMConfig.borderText + option1 + ".png"
	#Path to the background image
	backpath = IMConfig.backgroundPath + IMConfig.backgroundText + option2 + ".png"

	#Opens all of the images needed and converts them to RGBA
	unitImage = PIL.Image.open(path).convert("RGBA")
	unitBorder = PIL.Image.open(borderpath).convert("RGBA")
	unitBack = PIL.Image.open(backpath).convert("RGBA")

	#Actual merging of the images
	unitImage.paste(unitBorder, (0,0), unitBorder)
	unitBack.paste(unitImage, (0,0), unitImage)

	#Saves the images
	unitBack.save(number + ".png")


#Gets User input so that it can be run from the command line
try:
	userInput = input("Input number, option1, and option2. All arguments must be in one set of quotation marks. Input _ for an empty option." + "\n")
	splitInput = userInput.split()
except:
	print("Error in input")
else:
	try:
		inputNumber = splitInput[0]
		inputOption1 = splitInput[1]
		inputOption2 = splitInput[2]
	except:
		print("Not enough valid arguments")
	else:
		#For empty options
		if(inputOption2 == "_"):
			inputOption2 = ""
		try:
			combineImages(inputNumber, inputOption1, inputOption2)
		except:
			print("Image(s) not found")




#Hard coded example
#combineImages("5092", "Yellow", "")