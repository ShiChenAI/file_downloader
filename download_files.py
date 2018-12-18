import os
import urllib.request
import os
import sys
from PIL import Image 
import socket

data_path = './data/'

def _progress(block_num, block_size, total_size):
    if total_size == 0:
        return
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
        for cnt, line in enumerate(f):
            items = line.split('\t')
            file_type = items[0]
            print('\n%d. %s' % (cnt, file_type))
            url = items[1]
            if file_type in targets:
                if not os.path.exists(data_path + file_type):
                    os.makedirs(data_path + file_type)
                
                file_name = data_path + file_type + '/' + url.split('/')[-1]
                file_name = file_name.strip('\n')
                print(file_name)
                try:
                    urllib.request.urlretrieve(url, file_name, _progress)
                    try:
                        im = Image.open(file_name)
                        im = im.convert('RGB')
                        im.save(data_path + file_type + '/' + get_file_name(file_name) + '.jpg')
                        os.remove(file_name)
                    except OSError:
                        print('File error.')
                        continue
                except TimeoutError:
                    print('Timeout')
                    continue
                except urllib.error.URLError:
                    continue
                except socket.timeout:
                    print('Timeout')
                    continue


def main():
    socket.setdefaulttimeout(15)
    url_file_name = 'vis10cat.txt'
    targets = ['PieChart']
    download(url_file_name, targets)

if __name__ == '__main__':
    main()