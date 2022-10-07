from datetime import datetime
import os


def generate_excel_file(filename, arr):
    '''
        generates the excel file from the list of the scraped data
    '''
    with open (filename + str(datetime.today().date()) +'__' +str(datetime.now().strftime("%H_%M_%S")) +'.xlsx', 'w') as f:
        for i in arr:
            for j in i:
                f.write(j.text)
                f.write('\t')
            f.write('\n')
    f.close()

    return str(os.path.abspath(f.name))
