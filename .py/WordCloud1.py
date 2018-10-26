import matplotlib.pyplot as plt
import jieba
import wordcloud
txt="心有猛虎，细嗅蔷薇。审视我的内心吧，亲爱的朋友，你应颤栗，因为那才是你本来的面目。"
w=wordcloud.WordCloud(width=1000,height=700,font_path = "msyh.ttc")
w.generate("".join(jieba.lcut(txt)))
w.to_file("myfirstWordCloud.jpg")
plt.imshow(w)
plt.axis("off")
plt.show()
