from wordcloud import WordCloud
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

def make_word_cloud_func(cleaned_text):
    wordcloud = WordCloud(background_color="white", width=960, height=960, margin=8).generate(cleaned_text)
    fig, ax = plt.subplots(figsize=(8,8))
    ax.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    
    #TODO elsa why can't we save the figure here?
    fig.savefig("../../../src/readme/capstone_2_readme/word_cloud.png")
    plt.close()



