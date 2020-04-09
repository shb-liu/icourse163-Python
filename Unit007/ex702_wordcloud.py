#ex702_wordcloud.py
import wordcloud
import jieba

c = wordcloud.WordCloud()
c.generate("wordcloud by Python")
c.to_file("pywordcloud.png")

txt = "计算机是运算工具，更是创新平台，高效有趣地利用计算机需要更简洁实用的编程语言。Python简洁却强大、简单却专业，它是当今世界最受欢迎的编程语言，学好它终身受用。请跟随我们，学习并掌握Python语言，一起动起来，站在风口、享受创新！"
w = wordcloud.WordCloud(width=1000, font_path="STHeiti Medium.ttc", height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("jieba.png")