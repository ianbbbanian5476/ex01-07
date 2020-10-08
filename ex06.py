myDict1 = {'dog':'狗','cat':'貓'}
myDict2 = {'狗':'dog','貓':'cat'}

print('歡迎使用只知道狗和貓的多功能字典')
print('使用以下指令開始使用:')
print('1. 英翻中 2. 中翻英 3. 離開')


while '1' == '1':
  a = input('請輸入指令:')
  if a == '1':
    b = input('請輸入要查詢的英文單字:')
    print(b,'=>',myDict1[b])
    pass
  elif a == '2':
    c = input('請輸入要查詢的中文單字')
    print(c,'=>',myDict2[c])
    pass
  elif a == '3':
    break
  elif a != '1' or a != '2' or a != '3':
    print('請輸入正確指令!')
    pass
