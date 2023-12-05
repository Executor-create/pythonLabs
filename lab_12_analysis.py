import pandas as pd
import re
import matplotlib.pyplot as plt

with open('stopwords_ua.txt', 'r', encoding='utf-8') as f:
    stop_words_list = [line.strip().lower() for line in f]

df = pd.read_csv('pravda_data_cleaned.csv')

text = ' '.join(df['Text'])

words = re.findall(r'\b\w+\b', text, flags=re.UNICODE)

words = [word.lower() for word in words]

filtered_words = [word for word in words if word not in stop_words_list]

df_word_freq = pd.DataFrame(filtered_words, columns=['Слово'])

word_freq = df_word_freq['Слово'].value_counts().reset_index()
word_freq.columns = ['Слово', 'Частота']

df_word_freq_sorted = word_freq.sort_values(by='Частота', ascending=False).reset_index(drop=True)

df_word_freq_sorted.to_csv('pravda_data_word_freq.csv')

top_15_words = df_word_freq_sorted.head(15)
plt.bar(top_15_words['Слово'], top_15_words['Частота'])
plt.xlabel('Слово')
plt.ylabel('Частота')
plt.title('15 найпопулярніших слів')
plt.xticks(rotation=45, ha='right')
plt.show()

df = pd.read_csv('pravda_data_cleaned.csv', parse_dates=['Date'])

def get_most_popular_word(row):
    words = re.findall(r'\b\w+\b', row, flags=re.UNICODE)
    words = [word.lower() for word in words]
    filtered_words = [word for word in words if word not in stop_words_list]
    word_freq = pd.Series(filtered_words).value_counts().reset_index()
    word_freq.columns = ['Слово', 'Частота']
    most_popular_word = word_freq.iloc[0]['Слово']
    return most_popular_word

df['Найпопулярніше Слово'] = df['Text'].apply(get_most_popular_word)

plt.bar(df['Date'], df['Найпопулярніше Слово'])
plt.xlabel('Дата')
plt.ylabel('Найпопулярніше Слово')
plt.title('Найпопулярніше слово з кожного місяця')
plt.xticks(rotation=45)
plt.show()
