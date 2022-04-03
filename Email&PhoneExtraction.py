pip install openpyxl
pip install googlesearch-python
pip install pandas
#packages
from openpyxl import load_workbook
from googlesearch import search
import pandas as pd

def findinglinks(outputfile):
    search_result_list = []
    search_result_name = []

    lst = []
    n = int(input("Enter lenght of name : "))

    for i in range(0, n):
        ele = input()
        lst.append(str(ele))
    without_empty_strings = [string for string in lst if string != ""]
    total = len(without_empty_strings)
    fail = 0

    for l in without_empty_strings:
        try:
            search_result = list(search(l + 'お問い合わせ' ,stop=2))
            search_result_list.append(search_result)
            search_result_name.append(l)
        except:
            fail+=1
        if total == len(search_result_name) - fail:
            break
        print('File completed: ' + str(len(search_result_name) - fail) + ' out of ' + str(total))
    dflink = pd.DataFrame(search_result_list, columns=['Link1', 'Link2']) 
    dflink['Company Name'] = pd.DataFrame(search_result_name)
    dflink.to_excel(outputfile, header=False, index= False)

findinglinks("output.xlsx")
