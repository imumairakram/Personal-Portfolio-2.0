with open('assets/App-BIMeU_XJ.js', 'r', encoding='utf-8') as f:
    code = f.read()

idx = code.find('var xl={')
print("Found xl at", idx)
print(code[idx-3500:idx+600])
