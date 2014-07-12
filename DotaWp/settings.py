# Scrapy settings for DotaWp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#     http://doc.scrapy.org/en/latest/topics/settings.html


BOT_NAME = "DotaWp"

SPIDER_MODULES = ["DotaWp.spiders"]
NEWSPIDER_MODULE = "DotaWp.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "DotaWP_Image_Crawler_Bot"

IMAGES_STORE = "./images"
IMAGES_EXPIRES = 90
ITEM_PIPELINES = {"scrapy.contrib.pipeline.images.ImagesPipeline": 1}

# Logging
LOG_ENABLED = True
#LOG_FILE = "log.txt"
LOG_LEVEL = "DEBUG"

# Max simultaneous page requests
CONCURRENT_REQUESTS = 2

# Max time while fetching page request
DOWNLOAD_TIMEOUT = 30

RETRY_TIMES = 5
# Don't hit the site too hard! Take it slow.
DOWNLOAD_DELAY = 2

# Item Storage
# Store items returned by the spiders
FEED_URI = "data.json"
# Item storage format
FEED_FORMAT = "json"
