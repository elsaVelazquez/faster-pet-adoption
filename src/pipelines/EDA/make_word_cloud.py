from wordcloud import WordCloud


wordcloud = WordCloud(background_color="white", width=960, height=960, margin=8).generate(cleaned_text)
fig, ax = plt.subplots(figsize=(8,8))
ax.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()