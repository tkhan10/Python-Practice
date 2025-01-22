import qrcode

data = 'This is QA Code Encode programm'

img = qrcode.make(data)

img.save('/Users/tofekkhan/qrcode/mycode.png')