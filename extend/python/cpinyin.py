from pypinyin import pinyin,Style,slug
def cvt(name):
    pinyin1=(slug(name, separator="")).upper()
    return pinyin1
