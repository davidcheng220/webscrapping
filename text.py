import requests
from bs4 import BeautifulSoup

def get_artical_string(artical_url: str)->str:
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }

    cookies = {
    "over18": "1",
    }

    # artical_url = "https://www.ptt.cc/bbs/Gossiping/M.1731081383.A.48A.html"
    res_artical = requests.get(artical_url, headers=headers, cookies=cookies)

    soup_artical = BeautifulSoup(res_artical.text, "html.parser")
    # ##
    soup_artical_content = soup_artical.select('div[id="main-content"]')[0]
    # # ## why not text?
    # div_artical = soup_artical_content.select('div[class="article-metaline"]')
    # # print(div_artical)

    # push_content = soup_artical_content.select('div[class="push"]')
    # # extract the div content
    # for div_artical in div_artical:
    #     div_artical.extract()

    # for push_content in push_content:
    #     push_content.extract()
    # 精簡化
    extract_att_list = [".article-metaline", ".push", ".article-metaline-right", ".richcontent", ".f2"]

    for att in extract_att_list:
        for tag in soup_artical_content.select(att):
            tag.extract()

    return soup_artical_content.text

if __name__ == "__main__":
    artical_url = "https://www.ptt.cc/bbs/Gossiping/M.1731081383.A.48A.html"
    print(get_artical_string(artical_url))