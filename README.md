# Wanton - full page screenshot app

As a product manager, I found myself taking screenshots of a bunch of sites with really long pages (I would then add annotations to the images for my developement and design team). Since I was just learning python, I decided to write my own script that could take a screen shot of the full web page. Enter Wanton - screenshot full webpages. Sense a bunch of modern single page apps leverage a lot of fancy animation, most screenshot apps I discovered wouldn't trigger the animations and would deliver an incomplete picture. Not Wanton, it does a good job of capturing what's really going on.

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

This is seriouly one of the simplest apps ever. Use your favorite terminal to get this sucker going.


## Running the tests

```

1. Go into the repo if you aren't already

cd wanton

2. Start the env if you haven't already

source env/bin/activate

3. Run the python script. It will take a screenshot of the following website: "http://paidpost.nytimes.com/milkpep/a-fresh-look.html"
python screenshot_manager.py

4. Wait about 15 seconds. The screenshot should pop-up once the script has finished running.

```


### Take screenshots of your favorite sites

I wrote this script to only work on web pages were you have to scroll. Otherwise just press shift-command-4 ;). 

```

1. Go into the repo if you aren't already

cd wanton

2. Start the env if you haven't already

source env/bin/activate

3. Add the url you want to take a screenshot of as a command line argument

python screenshot_manager.py https://www.wildwisdoms.com/

```

## Built With

I wrote this when I first began learning how to code. Junior then and junior now - I'll always be junior. Some of the biggest motivations to writing this script was to learn Pillow, Selenium, and Google Chrome Driver.

* [Pillow](https://pillow.readthedocs.io/en/latest/) - Python Imaging Library used for processing screenshots
* [Selenium](http://www.seleniumhq.org/) - Used for Web Driver Automation
* [Google Chrome Drive](https://sites.google.com/a/chromium.org/chromedriver/) - Web Driver of choice to watch the script in action.

## Contributing

Please contribute! I did this for fun but it would be cool to build this out and combine it with something else like...crop out the ads, write a visual recogniation algo using Tenserflow to identify brands and keep track of advertiser spends across the internet (I work in media lol). Visually verison control your competitors. Come-on, think of something better.....

## Authors

* **Justin Sullivan** - *Initial work* - [Linkedin](https://www.linkedin.com/in/justsull)


## Acknowledgments

* Hat tip to [Full Page Screen Capture](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl?hl=en-US) to do something better 


