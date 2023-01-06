import os
print(os.popen("fsutil fsinfo drives").read())
print(os.system('cmd /c "wmic logicaldisk list brief"'))