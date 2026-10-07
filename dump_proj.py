with open('assets/App-BIMeU_XJ.js', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('projects__stack')
if idx != -1:
    with open('scratch_projects.txt', 'w', encoding='utf-8') as out:
        out.write(content[idx-1500:idx+3500])
    print("Written to scratch_projects.txt")
else:
    print("Not found")
