import lxml.html as html
import requests


def get_all_links(main_domain):
    list_urls = list()
    for i in range(1, 4):
        domain = main_domain + 'page/' + str(i)
        req = requests.get(domain)
        page = html.fromstring(req.content)
        article_links = page.xpath(
            '//div[contains(@id, content)]/article/a/@href'
            )
        for x in article_links:
            list_urls.append(x)
    return list_urls


def get_info(urls):
    all_info = []
    for i in urls:
        req = requests.get(i)
        page = html.fromstring(req.content)
        title = page.xpath('//h1[contains(@class, entry-title)]//text()')
        body = page.xpath('//div[contains(@class, entry-content)]/p//text()')
        date_create = page.xpath(
            '//div[contains(@class, post-meta)]/ul/li/time//text()'
        )
        images = page.xpath('//div[contains(@class, "entry-content")]//img/@src')
        
        print(title)
        print(body)
        print(images)
        print(date_create)
        print()


def main():
    main_domain = 'https://tproger.ru/'
    urls = get_all_links(main_domain)
    get_info(urls)


if __name__ == "__main__":
    main()
