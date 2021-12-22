def operation(fv1, fv2, op):  # рефакторинг функции operation для проверки результата, который отправляет бот
    # Выполняем действие
    res = 0
    if op == 'Перевести':
        res = fv1*fv2
    elif op == 'Cтоимость электрогитары Gibson SG в рублях':
        res = 500.0/fv2
    return res


def num_input(text):  # рефакторинг функции ввода числа first_num для проверки правильного изменения состояния
    cond = False
    try:
        a = float(text)
    except ValueError:
        cond = True
    if not cond and a <= 0:
        cond = True

    if cond:
        return 'CURRENT_STATE'  # если ошибка ввода, то не меняем состояние
    else:
        return 'STATE_COURSE'  # если всё хорошо, то переходим к вводу курса