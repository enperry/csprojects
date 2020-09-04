import re

def parse(markdown):
    m = markdown
    m = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', m)
    m = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', m)
    m = re.sub(r'^\* (.*?$)', r'<li>\1</li>', m, flags=re.M)
    m = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', m, flags=re.S)
    for i in range(6, 0, -1):
        m = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), m, flags=re.M)
    m = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', m, flags=re.M)
    m = re.sub(r'\n', '', m)
    return m