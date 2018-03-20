import datetime


def ftime(t, f='%Y-%m-%d %H:%M'):
    t = t + datetime.timedelta(hours=8)
    try:
        return datetime.datetime.strftime(t, f)
    except Exception:
        return 'N/A'
