import string
sentence=input("type your sentence : ")
new_sentence=""
for x in sentence:
               if x not in string.punctuation :
                       new_sentence+=x
print(new_sentence)
#المشروع بيخلّي المستخدم يكتب جملة،
#والبرنامج يشيل منها كل علامات الترقيم زي:
#! , . ? : ; -
#ويطبع الجملة نظيفة من غيرهم.