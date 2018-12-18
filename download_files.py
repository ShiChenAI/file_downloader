import os
import urllib.request
import os
import sys
from PIL import Image 

data_path = './data/'

def _progress(block_num, block_size, total_size):
    float_process = float(block_num * block_size) / float(total_size) * 100.0
    if float_process > 100:
        float_process = 100
    sys.stdout.write('\r>> Downloading %.1f%%' % (float_process))
    sys.stdout.flush()


def get_file_name(file_path):
    (filepath,tempfilename) = os.path.split(file_path)
    (filename,extension) = os.path.splitext(tempfilename)
    return filename


def download(url_file_name, targets):
    with open(url_file_name, 'r') as f:
        line = f.readline()
        while line:
            items = line.split('\t')
            file_type = items[0]
            print(file_type)
            url = items[1]
            if file_type not in targets:
                continue

            if not os.path.exists(data_path + file_type):
                os.makedirs(data_path + file_type)

            
            file_name = data_path + file_type + '/' + url.split('/')[-1]
            print(file_name)
            urllib.request.urlretrieve(url, file_name, _progress)
            im = Image.open(file_name)
            im = im.convert('RGB')
            im.save(data_path + file_type + '/' + get_file_name(file_name) + '.jpg')
            os.remove(file_name)


def main():
    url_file_name = 'vis10cat.txt'
    targets = ['LineGraph', 'BarGraph', 'PieChart']
    download(url_file_name, targets)

if __name__ == '__main__':
    main()