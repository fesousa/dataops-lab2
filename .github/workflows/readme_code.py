import re
with open('README.md') as readme:
    content = readme.read()
    subs = re.findall(r'```.*?\n\$\{(.*?\)}```')
    print(subs)
