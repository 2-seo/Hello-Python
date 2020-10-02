# f = open('test.txt', 'w', encoding='utf-8')
# f.write('hi python!\n')
# f.write('hi python!\n')
# f.write('hi python!\n')
#
# f.close()


# import matplotlib.font_manager as fm
#
# # 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

# /System/Library/Fonts/Supplemental/AppleGothic.ttf

from wordcloud import WordCloud

removeTextList = ['ㅋ', '이모티콘', '"', '\n', '어떻게', '근데', '하는', '거야', '했어', '있어', '하면', '이거', '그냥', '너무',
                  '나도', '지금', '내가', '있는', '되는', '건가']

text = ''
with open('kakaotalk.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines[1:]:
        if line.find('","') > 0:
            for removeList in removeTextList:
                line = line.replace(removeList, '')

            text += line.split(',')[2]

# print(text)
font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'

# 일반 클라우드 사각형 모향으로 만들기
# wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

# 마스킹된 워드 클라우드 만들기
from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path=font_path, background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")


