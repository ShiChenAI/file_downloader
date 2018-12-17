import os
import urllib
import os
import sys

data_path = './data/'

def _progress(block_num, block_size, total_size):
    sys.stdout.write('\r>> Downloading %.1f%%' % (float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()


def download(url_file_name, targets):
    with open(url_file_name, 'r') as f:
        line = f.readline()
        while line:
            items = line.split('\t')
            file_type = items[0]
            url = items[1]
            if file_type not in targets:
                continue

            if not os.path.exists(data_path + file_type):
                os.makedirs(data_path + file_type)

            
            file_name = data_path + file_type + '/' + url.split('/')[-1]
            print(file_name)
            urllib.request.urlretrieve(url, file_name, _progress)


def main():
    url_file_name = 'vis10cat.txt'
    targets = ['LineGraph', 'BarGraph', 'PieChart']
    download(url_file_name, targets)

if __name__ == '__main__':
    main()