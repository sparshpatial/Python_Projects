
# Program to take screenshot
  
import pyscreenshot
  
# To capture the screen
image = pyscreenshot.grab()


# To display the captured screenshot 
image.show()
  
# To save the screenshot
#screenshot will be save as the name you specify .
image.save("screenshot.png")
