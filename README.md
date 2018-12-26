# Wanton - full web page screenshot app

As a product manager, I found myself taking screenshots of a wide array of sites with long web pages. In this process, I often found that many of the pages were longer than my screen so I was unable the capture the complete web page as one screenshot. As I was in the intial stages of learning python, I thought it would be a great opportunity to test my skills and write a script to solve this problem. Enter Wanton: a full page screenshot app. Through a simple command line trigger, you can easily take a screenshot of the full web page of any site.  Although many web pages leverage fancy animation, most screenshot apps will not trigger the animations and will deliver an incomplete image. Not Wanton, it does a good job of capturing the bigger picture.

# Checkout the demo below!

![](wantondemo.gif)


## Getting Started

```

1. Clone repo
git clone https://github.com/justsull/wanton.git

2. Go into repo
cd wanton

3. make a virtual environment
virtualenv -p python3 env

4. start the env
source env/bin/activate

5. install the requirements
pip install -r requirements.txt

```

### Prerequisites

Use your favorite terminal to get this app up and running.


## Running the tests

```

1. Go into the repo if you aren't already
cd wanton

2. Start the env if you haven't already
source env/bin/activate

3. Run the python script. It will take a screenshot of the following webpage http://paidpost.nytimes.com/milkpep/a-fresh-look.html
python screenshot_manager.py

4. Wait about 15 seconds. The screenshot should pop-up once the script has finished running.

```


### Take screenshots of your favorite sites

I wrote this script to only work on web pages where you have to scroll. Otherwise just press shift-command-4 ;). 

```

1. Go into the repo if you aren't already
cd wanton

2. Start the env if you haven't already
source env/bin/activate

3. Add the url you want to take a screenshot of as a command line argument
python screenshot_manager.py https://yoururlgoeshere.com

```

## Built With

I wrote this when I first began learning how to code. Some of the biggest motivations to writing this script was to learn Pillow, Selenium, and play with Google Chrome Driver.

* [Pillow](https://pillow.readthedocs.io/en/latest/) - Python Imaging Library used for processing screenshots
* [Selenium](http://www.seleniumhq.org/) - Used for Web Driver Automation
* [Google Chrome Drive](https://sites.google.com/a/chromium.org/chromedriver/) - Web Driver of choice to watch the script in action.

## Contributing

Please contribute! I did this for fun but it would be cool to build this out and combine it with something else like... write a visual recogniation algo using Tenserflow to identify brands and keep track of advertiser campaigns across the internet.

## Authors

* **Justin Sullivan** - [Linkedin](https://www.linkedin.com/in/justsull)


## Acknowledgments

* Hat tip to [Full Page Screen Capture](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl?hl=en-US) for motivating me to do something better 


