import os
import shutil
import sys

# encoding in case of path problems
with open("titles.txt",encoding=sys.getdefaultencoding()) as titles:
    titlist = titles.readlines()

# remove any unwanted formatting like linebreak
escapes = ''.join([chr(char) for char in range(1, 32)])
translator = str.maketrans('', '', escapes)

# get list of folder names without parsing through every file in those folders
foldlist = next(os.walk('.'))[1]

for fold in foldlist:
    # this line is just to deal with the full width space that was giving me problems
    fold.replace("\u3000","")
    for title in titlist:
        ttitle = title.translate(translator)
        if ttitle in fold:
            files = os.listdir('{0}'.format(fold))
            os.makedirs(os.path.join('{0}/{1}'.format(ttitle,fold)))
            for f in files:
                shutil.move('{0}/{1}'.format(fold,f),'{0}/{1}/{2}'.format(ttitle,fold,f))
            if len(os.listdir('{0}'.format(fold)))==0:
                os.rmdir(fold)
            continue
