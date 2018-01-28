from PIL import Image
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time
import sys
import traceback
import re
import os

test_url = 'http://paidpost.nytimes.com/milkpep/a-fresh-look.html'

class wanton:

    def __init__(self):
        self.approach = "bottomup"  # topdown or bottomup
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver/chromedriver')

    def master(self, url):
        
        # setup folders and driver
        padding = self.setUp(url)

        # allow time to load page before determining dimensions
        time.sleep(3)

        # get the page and window dimensions
        yOffset, yPos, yDelta, xDelta, fullWidth, fullHeight, windowHeight = self.getDimensions(padding)

        # scroll down the page to initiate any animations
        self.scrollfullpage(fullHeight)

        # find screenshot positions, adjusted widths and heights accordingly given the padding
        arrangements = self.getPositions(yOffset, yPos, yDelta, xDelta, fullWidth, fullHeight)

        # arrange positions based on the approach
        arrangements = self.arrangePositions(arrangements)

        # take a screenshot at the provided positions
        images = self.processArrangements(arrangements, url)
        cropped_images = []
        total_height = 0
        total_width = 0
        start = len(images) - 1 if self.approach == "bottomup" else 0
        stop = -1 if self.approach == "bottomup" else len(images)
        step = -1 if self.approach == "bottomup" else 1

        # crop images to cut out the padding
        for i in range(start, stop, step):
            filename = images[i]
            im = Image.open(filename)
            im_width, im_height = im.size
            top_crop = 0 if i == start else padding * 2
            top_crop = (windowHeight) if i == (stop - step) else top_crop
            bounding_box = (0, top_crop, im_width,
                            im_height)  # using padding as the top border y axis coordinate to cut out the padding
            cropname = (('%s_cropped') % (i))
            crop_filename = self.crop_image(bounding_box, filename, cropname)
            cropped_images.append(crop_filename)
            total_height += (im_height - top_crop)
            total_width = total_width if total_width > im_width else im_width

        # stitch the screenshots together into one image
        stitched_filename = self.stitchScreenshots(cropped_images, total_width, total_height)
    
        self.clear_tmp()

        self.driver.quit()

    def setUp(self, url):
        directory = 'screenshots'
        full = 'screenshots/full'
        tmp = 'screenshots/tmp'
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.makedirs(full)
            os.makedirs(tmp)
        else:
            if not os.path.exists(full):
                os.makedirs(full)
            if not os.path.exists(tmp):
                os.makedirs(tmp)

        padding = 300

        # set initial window size
        print("Loading Page: {}".format(url))

        self.setWindow(1600, 2000)

        self.driver.get(url)
        
        

        return padding

    def setWindow(self, width, height):

        # set window size
        set_width = width
        set_height = height
        self.driver.set_window_size(set_width, set_height)

    def scrollfullpage(self, fullHeight):

        # scroll down the page by the height of the window
        for i in range(0, fullHeight, 800):
            x = 0
            y = i
            self.driver.execute_script("window.scrollTo(%s,%s)" % (x, y))
            time.sleep(.1)

    def getDimensions(self, padding):

        '''view_port = driver.get_window_size()
        view_width = view_port['width']
        view_height = view_port['height']'''
        body_height = self.driver.execute_script("return document.body.scrollHeight;")
        widths = self.driver.execute_script(
            "return widths = [document.documentElement.clientWidth, document.body ? document.body.scrollWidth : 0, document.documentElement.scrollWidth, document.body ? document.body.offsetWidth : 0, document.documentElement.offsetWidth ]")
        heights = self.driver.execute_script(
            "return heights = [document.documentElement.clientHeight, document.body ? document.body.scrollHeight : 0, document.documentElement.scrollHeight, document.body ? document.body.offsetHeight : 0, document.documentElement.offsetHeight]")
        fullWidth = max(widths)
        fullHeight = max(heights)
        windowWidth = self.driver.execute_script("return window.innerWidth")
        windowHeight = self.driver.execute_script("return window.innerHeight")

        # calculate delta's and set x, y coordinates of initial screen positioning relative to the entire screen
        yDelta = windowHeight - (padding if windowHeight > padding else 0)
        xDelta = windowWidth
        yPos = 0  # original was fullHeight - windowHeight
        xPos = None
        yOffset = fullHeight % yDelta

        # During zooming, there can be weird off-by-2 types of things...
        if (fullWidth <= xDelta + 2):
            fullWidth = xDelta

        # print("Full Width: " + str(fullWidth))
        # print("Full Height: " + str(fullHeight))
        # print("Body Height: " + str(body_height))
        # print("Window Width: " + str(windowWidth))
        # print("Window Height: " + str(windowHeight))
        # print("yOffset: " + str(yOffset))

        return yOffset, yPos, yDelta, xDelta, fullWidth, fullHeight, windowHeight

    def getPositions(self, yOffset, yPos, yDelta, xDelta, fullWidth, fullHeight):
        # Determine x, y coordinates of all necessary screen positionings to capture the entire screen when taking screenshots
        arrangements = []

        yPos = yPos
        yStop = fullHeight - yDelta

        while (yPos < yStop):
            xPos = 0
            while (xPos < fullWidth):
                arrangements.append([xPos, yPos])
                xPos += xDelta
            yPos += yDelta

        return arrangements

    def arrangePositions(self, arrangements):
        # arranges positions based off approach
        if self.approach == "topdown":
            arrangements = arrangements
        elif self.approach == "bottomup":
            arrangements = arrangements[::-1]

        return arrangements

    def processArrangements(self, arrangements, url):

        images = []

        # Disable all scrollbars when taking the screenshots
        self.driver.execute_script("document.body.style.overflowY = 'hidden';")

        # rotate through the list of positions

        for i, (x, y) in enumerate(arrangements):
            x = x
            y = y
            # print(("Scrolling to: %s, %s") % (x, y))
            
            print("Processing...")

            # scroll down the page by the height of the window
            self.driver.execute_script("window.scrollTo(%s,%s)" % (x, y))

            # time to load
            time.sleep(.5)

            # create image name, add the file name and coordinates to a list, take and save the screenshot under that name
            url_tiny = url[28:34]
            url_tiny = re.sub('\/+', "", url_tiny)  # substitute / character with nothing
            filename = (("screenshots/tmp/%s_screenshot_%s.png") % (url_tiny, i))
            images.append(filename)
            self.driver.get_screenshot_as_file(filename)

        print("Screenshot saved at screenshots/full/")
        return images

    def element_location(self, element):  # determines location of an element on a screen
        element_coordinates = (
            element.location['x'],  # left side coordinate
            element.location['y'],  # upper side coordinate
            (element.location['x'] + element.size['width']),  # right side coordinate
            (element.location['y'] + element.size['height'])  # bottom side coordinate
        )

        # because I am on a retina device, I have to double the coordinates, BRITTLE
        element_coordinates = [x * 2 for x in element_coordinates]

        print(element_coordinates)

        return element_coordinates

    def crop_image(self, coordinates, original_filename, crop_filename):  # crops an image and saves it to a new file

        # find the location of the container in pixels
        bounding_box = coordinates

        # open screenshot and crop it
        base_image = Image.open(original_filename)
        cropped_image = base_image.crop(bounding_box)
        base_image = base_image.resize(cropped_image.size)
        base_image.paste(cropped_image, (0, 0))

        # save the cropped screenshot
        crop_filename = (('screenshots/tmp/%s.png') % (crop_filename))
        base_image.save(crop_filename)

        # print("Saved Screenshot: " + crop_filename)

        return crop_filename

    def stitchScreenshots(self, images, total_width, total_height):
        # iterate through screenshots and stitch the images together from the top of webpage down, does not take into account landscape stitching

        stitched_image = Image.new('RGB', (total_width, total_height))

        y_offset = 0
        filename = ''
        for im in images:
            im = Image.open(im)
            stitched_image.paste(im, (0, y_offset))
            y_offset += im.size[1]
            filename = (("screenshots/full/%s.png") % (im))
        stitched_image.save(filename)
        stitched_image.show()

        return filename

    def clear_tmp(self):
        # clear tmp folder
        dirPath = 'screenshots/tmp'
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath+"/"+fileName)

    def cropStuff(self, stuff, stitched_filename):

        for thing in stuff:
            element_name = thing

            # BRITTLE - this is lazy coding, see if class works, if not its probably an id instead
            try:
                element = self.driver.find_element_by_class_name(element_name)
            except:
                element = self.driver.find_element_by_id(element_name)

            # grab x, y coordinates of the element
            coordinates = self.element_location(element)

            # crops an image at the provided coordinates and saves it as the provided filename
            original = stitched_filename
            self.crop_image(coordinates, original, element_name)

    '''def animations_exist(self):
        css_animations = {
            'transition': ['property', 'seconds'],
            'transform':[
                'translate':['x_pixels','y_pixels'],
                'rotate':'degrees',
                'scale':['multiply_width','multiply_height'],
                'skewX':'degrees',
                'skewY':'degrees',
                'skew':['x_degrees','y_degrees'],
                'matrix':['scaleX','skewY','skewX','scaleY','translateX','translateY'],
                'rotateX':'degrees',
                'rotateY':'degrees',
                'rotateZ':'degrees'],
            'animation':'seconds'}'''


if __name__ == '__main__':
    try:
        if len(sys.argv)>1:
            url = sys.argv[1]
        else:
            url = test_url
        w = wanton()
        driver = w.driver
        w.master(url)
    except Exception as exc:
        print(exc)
        traceback.print_exc(file=sys.stdout)
        driver.quit()

