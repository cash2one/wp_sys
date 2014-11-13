# -*- coding: utf-8 -*-
import re
import requests
from pyquery import PyQuery as pq
from sqlalchemy import exc


def filmav_grab_article_url(website_index="http://filmav.com/"):
    headers = {
        'Host': 'filmav.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn,en;q=0.7,en-us;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    r = requests.get(url=website_index, headers=headers)

    if r.status_code is not 200:
        s = "首页抓取不是200,返回状态码：" + str(r.status_code)
        print s
        return s

    h = pq(r.text)
    article_urls_htmlelements = h('.more-link')
    article_urls = []
    for url in article_urls_htmlelements:
        u = url.attrib['href'].split("#")[0]
        article_urls.append(u)

    return article_urls


# def filmav_grab_article_body(url='http://filmav.com/52661.html'):
def filmav_grab_article_body(url='http://www.iplaysoft.com/hackertyper.html'):
    headers = {
        'Host': 'filmav.com',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-cn,en;q=0.7,en-us;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }

    r = requests.get(url=url)

    if r.status_code is not 200:
        s = "首页抓取不是200,返回状态码：" + str(r.status_code)
        print s
        return s

    h = pq(r.text)
    body = h('.entry-content')
    # 匹配中文，记得要进行编码
    str1 =str(unicode(body).encode('utf-8'))


    res = r'(.*)<h3>写在后面：</h3'
    newbody = re.compile(res)
    m = re.findall(newbody, unicode(body).encode('utf-8'))
    for im in m:
        print im



    print type(str(unicode(body).encode('utf-8')))



def filmav_save_article_url(article_urls, session, model_url):
    website = 'filmav.com'
    for url in article_urls:
        url_instance = model_url(url=url, website=website)
        session.add(url_instance)
        try:
            session.commit()
        except exc.IntegrityError, e:
            print "捕获异常(链接已经存在）： " + e.message
            session.close()


if __name__ == '__main__':
    filmav_grab_article_body()

