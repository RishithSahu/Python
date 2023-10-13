books_data = '''Kanada Kuvempu Madhumagalu
Kanada Kuvempu ramayannadarshanam
English r_k_narayana malgudi_days
English r_k_narayana Dateless_diary
Sanskrit Bhasa Swapanavasavadatta
Sanskrit Kalidasa Raghuvamasha
'''
#Find no of books
print("No. of books = ",len(set(books_data.split("\n"))))

#Find no of languages
langs = set()
for data in books_data.splitlines():
    lang = data.split()[0]
    langs.add(lang)
print('No. of languages = ',len(langs))
#Find no of authors
#display the list of books in each language

lang_book={}

for data in books_data.splitlines():

d=data.split()

lang,name=d[0],d[1]

if lang not in lang_book:

lang_book[lang]=set()

lang_book[lang].add(name)

print(lang_book)

for lang in lang_book:

print(lang,"--->")

for name in lang_book[lang]:

print("\t",name)