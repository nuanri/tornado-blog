import math

import settings


def get_info(handler):

        try:
            cur_page = int(handler.get_argument("page", 1))
            page_size = int(handler.get_argument("page_size", settings.PAGE_SIZE))
        except:
            cur_page = 1
            page_size = settings.PAGE_SIZE

        start = (cur_page-1)*page_size
        stop = start + page_size

        return (cur_page, page_size, start, stop)


def custom_rule(cur_page, total, page_size, path_url):
    '''分页样式，当前页码，前五页，后五页模式
    '''
    # 获取的最大页码数
    max_page = math.ceil(total/int(page_size))
    space_number = settings.SPACE_NUMBER

    # 最大页小于第一间隔数
    if max_page <= space_number:
        start_page = 1
        end_page = max_page + 1
        plist = [start_page, end_page]

    else:
        # 但前页小于第一间隔数
        if cur_page <= space_number:
            start_page = 1
            end_page = cur_page + space_number
            plist = [start_page, end_page]
        else:
            # 最大页面不到结尾的间隔数
            if max_page < cur_page + (space_number-1):
                start_page = abs(cur_page-(space_number-1))
                end_page = max_page + 1
                plist = [start_page, end_page]
            else:
                # 最大页面大于等于结尾的间隔数
                start_page = abs(cur_page-(space_number-1))
                end_page = cur_page + space_number
                plist = [start_page, end_page]

    if cur_page > 1:
        has_pre = cur_page - 1
    else:
        has_pre = 0
    if cur_page + 1 <= max_page:
        has_next = cur_page + 1
    else:
        has_next = 0

    def page_url(cur_page):
        return custom_url(path_url, cur_page)

    d = {
        "plist": plist,
        "has_pre": has_pre,
        "has_next": has_next,
        "cur_page": cur_page,
        "page_url": page_url
    }

    return d


def custom_url(path_url, cur_page):
    '''定制页码的url
    '''

    from urllib.parse import urlparse, urlsplit, parse_qsl, urlencode

    if '?' not in path_url:
        page_url = path_url + '?page=' + str(cur_page)
        return page_url

    # /?keyword=向日葵&page=2
    new = []
    find_page = False
    path = urlsplit(path_url).path
    query = urlsplit(path_url).query
    params = parse_qsl(query)
    for k, v in params:
        if k == 'page':
            v = cur_page
            find_page = True
        new.append([k, v])

    # /?keyword=向日葵
    if not find_page:
        new.append(["page", cur_page])

    page_url = '?'.join([path, urlencode(dict(new))])
    return page_url
