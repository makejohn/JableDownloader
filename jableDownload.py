import requests
import re
import sys
import os

url = "https://jable.tv/videos/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/106.0.0.0 "
                  "Safari/537.36 "
}


# get all url which end with .m3u8 from specific url
def get_m3u8_url(av_code):
    return re.findall(r'https.*?\.m3u8', requests.get(url + str(av_code) + '/', headers=headers).text)


def findM3u8(av_code):
    return re.findall("https.*m3u8", requests.get(url + av_code + '/', headers=headers).text)

def download_m3u8(m3u8):
    command = "m3u8d -u " + str(m3u8[0]) + " -o " + str(av_code)
    os.system(command)

if __name__ == '__main__':

    # Get Code
    if len(sys.argv) <= 2:
        print("Please enter the right code, Eg \"juq-071\"")
        exit(0)
    av_code = sys.argv[1]

    if sys.argv[2] == 'p':
        print(get_m3u8_url(av_code))
        exit(0)
    if sys.argv[2] == 'd':
        print(download_m3u8(findM3u8(av_code)))
