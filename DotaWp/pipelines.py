# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Nothing has been changed here. Default scrapy file.

class DotawpPipeline(object):
    def process_item(self, item, spider):
        return item
