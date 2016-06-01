from subprocess import check_output
from os import listdir

if __name__ == '__main__':
    answer = 0
    for f in listdir('files'):
        output = check_output(['tesseract', '-psm', '8', 
            'files/'+f, 'stdout', 'nobatch', 'digits'])
        answer += int(output, 2)
    print('Total sum is {0}'.format(answer))
    
