#Helpファイルの文言を置き換える
#cha1ra2018.03.08
#MIT Lisense

import csv
import shutil
from distutils import dir_util
import folder_map

dir_util.copy_tree(folder_map.get() + 'src/', folder_map.get() + 'input/')

with open(folder_map.get() + 'words_utf8.csv', encoding = 'utf-8_sig') as csvfile:
    spamreader = csv.reader(csvfile)
    for csvrow in spamreader:
        if csvrow[2] != '404':
            input_path = folder_map.get() + 'input/' + csvrow[0]
            output_path = folder_map.get() + 'output/' + csvrow[0]
            with open(input_path, 'r') as htmlfile:
                with open(output_path, 'w') as outputfile:
                    searchWord = '［***' + csvrow[1] + '***］'
                    for htmlrow in htmlfile:
                        outputrow = ''
                        if searchWord in htmlrow:
                            outputrow =  htmlrow.replace(searchWord, csvrow[2])
                            print(csvrow[1] + 'を' + csvrow[2] + 'に置き換え')
                        else:
                            outputrow = htmlrow
                        outputfile.write(outputrow)
            shutil.copyfile(output_path, input_path)