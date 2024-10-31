for item in tweets:
    doc = nlp(item)
    input_polarity = doc._.polarity
    sentiment = {'tweet': item, 'score': input_polarity}
    print(sentiment)
