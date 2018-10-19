'''
词云流程大致分两部分：调用jieba分词、调用wordcloud画图
1、分词：
    利用jieba把文章拆分成以空格为间隔的字词
2、画图：
    利用 wordcloud 时注意：
    a)、背景图的横纵尺寸应小于背景颜色图
    b)、如果文章为中文，则必须指定 WordCloud 对象的 font_path 为中文字体文件，否则乱码
'''

import jieba
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


def replaceString(text, oldStringList, newString):
    for old in oldStringList:
        text = text.replace(old, newString)
    return text


def getFileContent(filePath):
    content = ''
    with open(filePath, mode='r', encoding='utf8') as f:
        content = replaceString(f.read(), ['\n\r'], '')
    return content


def cutText(filePath):
    text = getFileContent(filePath)
    return ' '.join([word.strip() for word in jieba.cut(text, cut_all=False, HMM=True) if len(word.strip()) > 1])


def main():
    text = cutText('./chinesereport.txt')

    image_mask = imread('heart.jpeg')
    image_color = ImageColorGenerator(image_mask)
    bg_mask = imread('colorful.jpeg')
    bg_color = ImageColorGenerator(bg_mask)

    wc = WordCloud(
        font_path='/usr/share/fonts/STXINGKA.TTF',
        margin=2,
        mask=image_mask,
        color_func=bg_color,
        max_words=150,
        min_font_size=4,
        stopwords=None,
        background_color='white',
        max_font_size=150)
    wc.generate_from_text(text)
    wc.to_file('output.jpg')


if __name__ == '__main__':
    main()
