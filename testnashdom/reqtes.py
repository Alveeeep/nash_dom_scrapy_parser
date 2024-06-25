import requests
import json

url = "https://xn--80az8a.xn--d1aqf.xn--p1ai/%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B/%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3-%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B5%D0%BA/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2/%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA?place=0-1&objStatus=0"

payload = json.dumps({
  "api_key": "f61071560a4675aef2cba9815dc4599d",
  "events": [
    {
      "device_id": "lxt4u4b6.y5",
      "event_type": "fail_to_install",
      "event_properties": {
        "accountId": "roscap",
        "siteId": "pl27969",
        "domain": "xn--80az8a.xn--d1aqf.xn--p1ai",
        "error": "SecurityError: Failed to register a ServiceWorker for scope ('https://xn--80az8a.xn--d1aqf.xn--p1ai/') with script ('https://xn--80az8a.xn--d1aqf.xn--p1ai/sendsay_push_sw.js'): The script resource is behind a redirect, which is disallowed."
      },
      "os_version": "Win32",
      "platform": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
    }
  ]
})
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'no-cache',
  'cookie': 'spid=1719001576402_9fdc641717c3a5889ab5df324a01b43d_w1xs7i7wcl91une0; _ym_uid=1719001577970054836; _ym_d=1719001577; _ym_isad=2; spsc=1719240967845_4eeaf5c0b3f2cdc71112fc030a47367a_2dc4c47e5beb4aae25be080fa9d16c8093e7e989cef732b63b8bada59af3d7da',
  'pragma': 'no-cache',
  'sec-ch-ua': '"Opera GX";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
  'Referer': '',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0',
  'referer': 'https://xn--80az8a.xn--d1aqf.xn--p1ai/',
  'Accept': '*/*',
  'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Sec-Fetch-Dest': 'script',
  'Sec-Fetch-Mode': 'no-cors',
  'Sec-Fetch-Site': 'cross-site',
  'origin': 'https://xn--80az8a.xn--d1aqf.xn--p1ai',
  'authorization': 'Basic MTpxd2U=',
  'Service-Worker': 'script',
  'content-type': 'application/json',
  'access-control-request-headers': 'content-type',
  'access-control-request-method': 'POST',
  'content-length': '0',
  'Purpose': 'prefetch',
  'Sec-Purpose': 'prefetch;prerender',
  'Upgrade-Insecure-Requests': '1',
  'purpose': 'prefetch',
  'sec-purpose': 'prefetch;prerender'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
