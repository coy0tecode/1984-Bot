def judge():
    import s2t
    from nltk.stem import WordNetLemmatizer
    # Import Pickle
    import pickle
    

    # Read in audio stream for the user and convert to lowercase text
    audio_text = s2t.from_audio_file()


    # Convert text to array and tokenize
    tizer = WordNetLemmatizer()

    audio_text = audio_text.split()
    audio_text = [tizer.lemmatize(word) for word in audio_text]
    audio_text = ' '.join(audio_text)
    print(audio_text + '\n\n')

    with open('audio_text.txt', 'w') as audio_text_file:
        audio_text_file.write(audio_text)
    


    with open('audio_text.txt', 'r') as audio_text_file: 
        loaded_cvec = pickle.load(open('count_vectorizer', 'rb'))
        loaded_model = pickle.load(open('linear_svc', 'rb'))
        result = loaded_model.predict(loaded_cvec.transform(audio_text_file).toarray())
        print(result)
        return result
    
judge()