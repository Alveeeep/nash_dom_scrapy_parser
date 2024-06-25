import scrapy
import json


class ParseSpider(scrapy.Spider):
    name = "parse"
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "http": "scrapy_impersonate.ImpersonateDownloadHandler",
            "https": "scrapy_impersonate.ImpersonateDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }
    base_url = 'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/'
    api = 'api/kn/object?offset=%s&limit=20&sortField=obj_publ_dt&sortType=desc&place=0-1&objStatus=0'
    'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/kn/object?offset=40&limit=20&sortField=obj_publ_dt&sortType=desc&place=0-1&objStatus=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/110.0.0.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Sec-Ch-Ua': "'Opera GX';v='109', 'Not:A-Brand';v='8', 'Chromium';v='123'",
        'Sec-Ch-Ua-Platform': "'Windows'",
        'Sec-Fetch-Site': "same-origin",
        'Upgrade-Insecure-Requests': "1",
        'Authorization': 'Basic MTpxd2U ='
    }
    start_urls = [
        'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3-%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BA/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA?place=0-1&objStatus=0']
    offset = 0
    total = 0

    def parse(self, response):
        api_url = self.base_url + self.api % 0
        yield scrapy.Request(url=api_url, method='GET', headers=self.headers, callback=self.parse_api,
                             meta={"impersonate": 'chrome110'})

    def parse_api(self, response):
        url = 'https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/api/object/'
        data = json.loads(response.text)
        data = data['data']
        self.total = data.get('total')
        for el in data.get('list', []):
            id = el.get('objId')
            yield scrapy.Request(url=url + str(id), method='GET', headers=self.headers, callback=self.parse_page,
                                 meta={"impersonate": 'chrome110'})
        if self.offset < self.total:
            self.offset += 20
            yield scrapy.Request(url=self.base_url + self.api % self.offset, method='GET', headers=self.headers,
                                 callback=self.parse_api, meta={"impersonate": 'chrome110'})

    def parse_page(self, response):
        data = json.loads(response.text)
        data = data['data']
        res = {}
        res['name'] = data.get('nameObj')
        res['address'] = data.get('address')
        res['id'] = data.get('id')
        res['commissioning'] = data.get('objReady100PercDt')
        res['developer'] = data.get('developer')['orgForm']['shortForm'] + ' ' + data.get('developer')['devShortNm']
        res['group'] = data.get('developer')['developerGroupName'] if 'developerGroupName' in data.get('developer') else None
        res['publDate'] = data.get('objPublDt') if 'objPublDt' in data else None
        res['keysDate'] = data.get('objTransferPlanDt') if 'objTransferPlanDt' in data else None
        res['avgPrice'] = data.get('objPriceAvg') if 'objPriceAvg' in data else None
        res['soldOutPerc'] = data.get('soldOutPerc') if 'soldOutPerc' in data else None
        res['objClass'] = data.get('objLkClassDesc') if 'objLkClassDesc' in data else None
        res['flatCount'] = data.get('objElemLivingCnt') if 'objElemLivingCnt' in data else None
        yield {'data': res}
