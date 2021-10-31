import re
with open('README.md') as readme:
    content = readme.read()
    subs = re.findall(r'```.*?\n\($\{.*?\})\n```')
    print(subs)
