Please refer to the [License file](/LICENSE.txt) for the licensing of the project.

**Project** - DotaWp.com Wallpaper Crawler  
**Creator** - Ashish Nitin Patil aka !mmorta!  
**Created** - 19th of February, 2014  


###Project Summary

* Using Scrapy's CrawlSpider, we crawl the [DotaWP](http://www.dotawp.com) website.
* This fetches all images in the [images/full](/DotaWp/images/full) directory.
* The [rename_files.py](/DotaWp/rename_files.py) then renames all images with their corresponding title.


###Instructions for Crawling

* Either [download](https://github.com/ashishnitinpatil/dotawp_crawler/archive/master.zip) [this repository]() or clone it on your machine  
    `git clone https://github.com/ashishnitinpatil/dotawp_crawler.git <local_dir>`
* Install python 2.7 or later on your machine  
    Refer to the official [Beginner's guide](https://wiki.python.org/moin/BeginnersGuide/Download) if you don't know how.
* Install scrapy on your machine  
    Refer to the [scrapy docs](http://scrapy.readthedocs.org/en/latest/intro/install.html) for that.
* Now `cd` to your downloaded DotaWP project directory.  
    `cd <path_to_dotawp_dir>/DotaWp`
* Execute the crawl  
    `python -m scrapy crawl dotawp`
* Let the crawling finish. (time taken depends on number of images, project settings)  
    You can see the progress in the [logs](/DotaWp/logs.txt)
* Rename the files by running the [rename_files](/DotaWp/rename_files.py) script.  
    You can double click the file or run the below command.  
    `python rename_files.py`

That's it! Now you have all the DotaWp wallpapers in the images directory!
