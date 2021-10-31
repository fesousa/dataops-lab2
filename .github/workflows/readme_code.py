import re
with open('README.md', 'r') as readme:
    content = readme.read()
    subs = re.findall(r'```.*?\n(\$\{.*?\})\n```', content)
    for s in subs:
        file = s[2:-1]
        with open(file) as f:
            content.replace(s, f.read())
    
with open('README.md', 'w') as readme:
    readme.write(content)