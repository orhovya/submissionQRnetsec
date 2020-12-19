# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import qrcode
import pyqrcode



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myfile = open("qrLink","w+")
    url = pyqrcode.create('~/Desktop/submissionQRnetsec/submission_html/subsys.html')
    url.svg('uca-url.svg', scale=8)
    url.eps('uca-url.eps', scale=2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
