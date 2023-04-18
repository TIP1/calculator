def calc():
    expr = input('Введите выражение:')
    if bool(set('{}[]').intersection(set(expr))):
        print('Вероятно некоррктные данные')
        calc()
    else:
        try:
            print(eval(expr))
        except:
            print('Вероятно некоррктные данные')
            calc()


calc()
