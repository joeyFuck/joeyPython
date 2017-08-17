try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
# 错误有多种可能
# except ValueError as e:
#     print ('ValueError:', e)
finally:
    print('finally...')
print('END')























