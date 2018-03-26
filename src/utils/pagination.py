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


def custom_rule(cur_page, total, page_size):
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

    d = {
        "plist": plist,
        "has_pre": has_pre,
        "has_next": has_next,
        "cur_page": cur_page
    }

    return d
