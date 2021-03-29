import pandas as pd

tab="        "
f = open('test.xml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<ЭДПФР xmlns="http://пф.рф/СИоЗП/2021-03-15" xmlns:УТ2="http://пф.рф/УТ/2017-08-21" xmlns:АФ5="http://пф.рф/АФ/2018-12-07">\n')
f.write(tab+'<СИоЗП>\n')
f.write(tab+tab+'<Организация>\n')
f.write(tab+tab+tab+'<УТ2:ИНН>'+'Эксель - 3'+'</УТ2:ИНН>\n')
f.write(tab+tab+tab+'<УТ2:КПП>'+'Эксель - 4'+'</УТ2:КПП>\n')
f.write(tab+tab+tab+'<ОКФС>'+'Эксель - 5'+'</ОКФС>\n')
f.write(tab+tab+tab+'<КТО>'+'Эксель - 6'+'</КТО>\n')

# Сортировка в экселе:
# год
#   month
#       фио


    
f.close()
