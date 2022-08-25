#13.12

def depozit(contribution,years,interest_rate):

    """
    Подсчитывает размер вклада за время лет под определенны процент
    :param contribution: float - размер первоначального вклада
    :param years: int -  количество лет размещения вклада
    :param interest_rate: float -  процентная ставка годовых
    :return: float - накопление под определенный процент за указанное количество лет
    """
    #for i in range(years):
        #contribution += contribution * interest_rate/100
    return (contribution* interest_rate/100 for i in range(years))

c = float(input("Введите сумму первоначального вклада:"))
y = int(input("На сколько лет размещаете депозит?:"))
p = float(input("Под какой процент годовых размещается вклад?:"))
print(depozit(c,y,p))