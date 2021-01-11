# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyqrcode



if __name__ == '__main__':
    url = pyqrcode.create('file:///home/amitmao/Desktop/submissionQRnetsec/submission_html/subsys.html')
    url.svg('uca-url.svg',background='white', scale=8)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
