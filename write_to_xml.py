import pandas as pd

tab="        "
f = open('test.xml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<ЭДПФР xmlns="http://пф.рф/СИоЗП/2021-03-15" xmlns:УТ2="http://пф.рф/УТ/2017-08-21" xmlns:АФ5="http://пф.рф/АФ/2018-12-07">\n')
f.write(tab+'<СИоЗП>\n')

f.close()
