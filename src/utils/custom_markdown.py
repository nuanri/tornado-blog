import markdown


def convert_html(body):
    extensions = ["tables", "nl2br", "codehilite", "fenced_code", "def_list"]
    ret = markdown.markdown(
        body,
        extensions,
        safe_mode=True,
        # safe_mode='escape',
        enable_attributes=False
    )

    return ret
