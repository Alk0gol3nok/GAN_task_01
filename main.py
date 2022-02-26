import random

print('Приветствую тебя, путник, ты  на арене! Твоя задача убить босса')

print('\n ***ТВОЙ АРСЕНАЛ ЗАКЛИНАНИЙ***')
print('№1 Василиск - призывает герою в помощь питомца, который наносит дпоолнительно 40 урона на 3 хода')
print('№2 Первая_помощь - мгновенно лечит героя на 50 ед. и даёт пассивное лечение (20 ед.) на 3 хода')
print('№3 Дымовая_шашка - накладывает слепоту на босса на 2 хода')
print('№4 Проливая_кровь - наносит 70 ед. урона и накладывает кровотечение на 2 хода')
print('№5 Щит_Ахилла - даёт ауру непобедимости на 5 ходов')
print('№6 Последний_вздох - герой выпивает зелье Афины, получая эффект "Последняя надежда"')
print('№7 Базовая_атака - герой наносит обычный удар равный своей атаке')

print('\n ***ИНФОРМАЦИЯ О НЕГАТИВНЫХ И ПОЛОЖИТЕЛЬНЫХ ЭФФЕКТАХ***')
print('1)"Слепота" - даёт невидимость герою (урон по герою не проходит)')
print('2)"Кровотечение" - отнимает дополнительно 50% от начальной атаки героя')
print('3)"Аура непобедимости" - повышает начальную защиту героя на 50%')
print('4)"Последняя надежда" - воскрешает героя при смерти, и восстанавливает 31 ед. здоровья')

print('\n ***УСЛОВИЯ ИСПОЛЬЗОВАНИЯ ЗАКЛИНАНИЙ***')
print('1)"Василиск" - можно применить не более 3 раз за игру, раз в 5 ходов')
print('2)"Первая помощь" - можно использовать 2 раза за игру')
print('3)"Дымовая шашка" - можно использовать раз в 5 ходов, не более 2 раз за игру')
print('4)"Проливая_кровь" - можно использовать на 5 ход игры, каждые 5 ход игры')
print('5)"Щит_Ахилла" - можно использовать только поcле применения "Василиска" или "Дымовой шашки",'
      ' раз в 5 ходов')
print('6)"Последний вздох" - можно использовать 1 раз за игру,'
      ' и только после применения 2 раз "Щит_Ахилла" и 2 раз "Первая_помощь"')


print('\n ***ИНФОРМАЦИЯ О ХАРАКТЕРИСТИКАХ ГЕРОЯ И КАК ОНИ ВЛИЯЮТ***')
print('Здоровье - просто плоский стат, при значении "0" - вы умираете и игра заканчивается')
print('Атака - тоже плоский стат, который без % соотношения отнимает здоровье у босса')
print('Защита - плоский стат, который отнимает от атаки босса - данное значение')

atack_hero = random.randint(10, 30)
def_hero = random.randint(1, 10)
heal_hero = random.randint(200, 400)

heal_boss = 600
atack_boss = 30

person_move = random.randint(0, 1)

print('\n ***НАЧИНАЕТСЯ ГЕНЕРАЦИЯ СЛУЧАЙНЫХ ХАРАКТЕРИСТИК ГЕРОЯ***')
print('Атака героя:', atack_hero)
print('Защитая героя:', def_hero)
print('Здоровье героя:', heal_hero)

print('\n *** НАЧИНАЕТСЯ ПОКАЗ ХАРАКТЕРИСТИК БОССА***')
print('Здоровье босса(фиксированное):', heal_boss)
print('Атака босса(фиксированная):', atack_boss)

print('\n ***НАЧИНАЕТСЯ ВЫБОР: ЗА КЕМ ПЕРВЫЙ ХОД***')
if person_move == 0:
    print('Право первого хода получает: герой')
else:
    print('Право первого хода получает: босс')

print('\n ***НАЧАЛО БИТВЫ***')

number_move = 1  # номер хода
spels_hero = ['Василиск', 'Первая_помощь', 'Дымовая_шашка',
              'Проливая_кровь', 'Щит_Ахилла', 'Последний_вздох', 'Базовая_атака']  # список заклинаний
recoil_vas = 0  # начальный откат заклинания "Василиск"
recoil_smoke = 0  # начальный откат заклинания "Дымовая_шашка"
recoil_blood = 0  # начальный откат заклинания "Проливая_кровь"
recoil_guard = 0  # начальный откат заклинания "Щит_Ахилла"

time_vas = 0  # количество использований заклинания "Василиск"
time_help = 0  # количество использований заклинания "Первая_помощь"
time_smoke = 0  # количество использований заклинания "Дымовая_шашка"
time_sigh = 0  # количество использований заклинания "Последний_вздох"
time_def = 0  # количество использований заклинания "Щит_Ахилла"
time_blood = 0  # количество использований заклинания "Проливая_кровь"
time_baz = 0  # количество использований заклинания "Базовая атака"

active_vas = 0  # переменная, определяющая активен навык "Василиск" или нет
active_help = 0  # переменная, определяющая активен навык "Первая_помощь" или нет
active_smoke = 0  # переменная, определяющая активен навык "Дымовая_шашка" или нет
active_blood = 0  # переменная, определяющая активен навык "Проливая_кровь" или нет
active_def = 0  # переменная, определюяющая активен навык "Щит_Ахилла" или нет
active_sigh = 0  # переменная, определяющая активен навык "Последний_вздох" или нет

count_active_vas = 0  # переменная, отвечающая за промежуток активности навыка "Василиск"
count_active_help = 0  # переменная, отвечающая за промежуток активности навыка "Первая_помощь"
count_active_smoke = 0  # переменная, отвечающая за промежуток активности навыка "Дымовая_шашка"
count_active_blood = 0  # переменная, отвечающая за промежуток активности навыка "Проливая_кровь"
count_active_def = 0  # перменная, отвечающая за промежуток активности навыка "Щит_Ахилла"
count_active_sigh = 0  # переменная, отвечающая за промежуток активности навыка "Последний_вздох"


def PrintHeal():  # функция, которая печатает здоровье героя и босса после хода
    print('Здоровье героя:', heal_hero, 'единиц')
    print('Здоровье босса:', heal_boss, 'единиц \n')



while True:
    print('\nХод номер:', number_move)
    if person_move == 0:
        print('\nХодит герой...')
        spell_hero = input('Введите заклинание для атаки: ')
        if spell_hero in spels_hero:
            if spell_hero == 'Василиск':
                if time_vas < 3:
                    if recoil_vas == 0:
                        print('Герой c Василиском наносят урон:', (atack_hero + 40), 'ед. урона')
                        heal_boss -= (atack_hero + 40)  # урон по боссу заклинанием
                        recoil_vas = 5  # количество ходов для отката навыка
                        active_vas = 1  # навык перешел в активное состояние
                        count_active_vas = 3  # пошел отчёт активности навыка
                        PrintHeal()
                        if recoil_smoke != 0:  # если при активации навыка "Василиск"
                            recoil_smoke -= 1  # - есть активный навык "Дымовая_шашка", то уменьшаем его кулдаун на 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        person_move = 1  # передаём ход боссу
                        number_move += 1  # увеличиваем счетчик хода на 1
                        time_vas += 1
                    else:
                        print('Вы забываете, что уже использовали это заклинание и пропускаете ход')
                        print('Заклинание находится ещё в откате:', recoil_vas, 'хода')
                        PrintHeal()
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        recoil_vas -= 1
                        person_move = 1
                        number_move += 1
                else:
                    print('Вы забываете, что уже использовали это заклинание более 3 раз, -  пропускаете ход')
                    PrintHeal()
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_blood != 0:
                        recoil_blood -= 1
                    recoil_vas -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == 'Первая_помощь':
                if time_help < 2:
                    print('Герой исцеляет себя на 50 ед. и 20 доп ед. здоровья')
                    heal_hero += 70
                    active_help = 1
                    count_active_help = 3
                    PrintHeal()
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_blood != 0:
                        recoil_blood -= 1
                    person_move = 1
                    number_move += 1
                    time_help += 1
                else:
                    print('Вы забываете, что уже использовали это заклинание более 2 раз, - пропускаете ход')
                    PrintHeal()
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_blood != 0:
                        recoil_blood -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == 'Дымовая_шашка':
                if time_smoke < 2:
                    if recoil_smoke == 0:
                        print('Герой кидает под себя дымовую шашку и скрывается из вида')
                        heal_hero += 30
                        recoil_smoke = 5
                        active_smoke = 1
                        count_active_smoke = 2
                        PrintHeal()
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        recoil_smoke -= 1
                        person_move = 1
                        number_move += 1
                        time_smoke += 1
                    else:
                        print('Вы забываете, что уже использовали это заклинание и пропускаете ход')
                        print('Заклинание находится ещё в откате:', recoil_smoke, 'хода')
                        PrintHeal()
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        recoil_smoke -= 1
                        person_move = 1
                        number_move += 1
                else:
                    print('Вы забываете, что уже использовали это заклинание более 2 раз, - пропускаете ход')
                    PrintHeal()
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_blood != 0:
                        recoil_blood -= 1
                    recoil_smoke -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == 'Проливая_кровь':
                if number_move >= 5:
                    if recoil_blood == 0:
                        print('Герой находит уязвимое место у босса и вызывает у него кровотечение')
                        heal_boss -= (70 + (atack_hero / 2))
                        recoil_blood = 5
                        active_blood = 1
                        count_active_blood = 2
                        PrintHeal()
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        recoil_blood -= 1
                        person_move = 1
                        number_move += 1
                        time_blood += 1
                    else:
                        print('Вы забываете, что уже использовали это заклинание и пропускаете ход')
                        print('Заклинание находится ещё в откате:', recoil_blood, 'хода')
                        PrintHeal()
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        recoil_blood -= 1
                        person_move = 1
                        number_move += 1
                else:
                    print('Вы попытались использовать заклинание, но из-за недостатка опыта - оно не сработало,'
                          'вы пропускаете ход')
                    PrintHeal()
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    recoil_blood -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == 'Щит_Ахилла':
                if number_move % 5 == 0:
                    if time_vas >= 1 and time_smoke >= 1:
                        active_def = 1
                        count_active_def = 5
                        time_def += 1
                        print('Герой отражает удар своим могучим щитом Ахилла и накладывает на себя защитную ауру')
                        def_hero += (def_hero / 2)
                        PrintHeal()
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_smoke != 0:
                            recoil_guard -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        recoil_guard -= 1
                        person_move = 1
                        number_move += 1
                    else:
                        print('Вы немного запутались в порядке выполнения заклинаний и пропускаете ход')
                        PrintHeal()
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        recoil_guard -= 1
                        person_move = 1
                        number_move += 1
                else:
                    print('Вы немного ошиблись в расчетах - когда нужно произносить заклинание и пропускаете ход')
                    PrintHeal()
                    if recoil_blood != 0:
                        recoil_guard -= 1
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    recoil_guard -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == "Последний_вздох":
                if time_sigh <= 1:
                    if time_def >= 2 and time_help >= 2:
                        print('Герой принимает божественное зелье, может когда-нибудь оно спасёт ему жизнь...')
                        active_sigh = 1
                        PrintHeal()
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        person_move = 1
                        number_move += 1
                        time_sigh += 1
                    else:
                        print('Вы немного запутались в порядке использований заклинаний и пропускаете ход')
                        PrintHeal()
                        if recoil_smoke != 0:
                            recoil_smoke -= 1
                        if recoil_guard != 0:
                            recoil_guard -= 1
                        if recoil_vas != 0:
                            recoil_vas -= 1
                        if recoil_blood != 0:
                            recoil_blood -= 1
                        person_move = 1
                        number_move += 1
                else:
                    print('Вы мешкаете и тянитесь за колбой с зельем, но она уже пустая, Вы потратили время в пустую'
                          'пропускаете ход...')
                    PrintHeal()
                    if recoil_vas != 0:
                        recoil_vas -= 1
                    if recoil_guard != 0:
                        recoil_guard -= 1
                    if recoil_blood != 0:
                        recoil_blood -= 1
                    if recoil_smoke != 0:
                        recoil_smoke -= 1
                    person_move = 1
                    number_move += 1
            elif spell_hero == 'Базовая_атака':
                print('Герой наносит обычный удар по боссу с базовой атаки:', atack_hero, 'единиц урона')
                heal_boss -= atack_hero
                PrintHeal()
                if recoil_smoke != 0:
                    recoil_smoke -= 1
                if recoil_guard != 0:
                    recoil_guard -= 1
                if recoil_vas != 0:
                    recoil_vas -= 1
                if recoil_blood != 0:
                    recoil_blood -= 1
                person_move = 1
                number_move += 1
                time_baz += 1
        else:
            print('В панике Вы произносите неправильно заклинание и впустую тратите ход')
            PrintHeal()
            if recoil_smoke != 0:
                recoil_smoke -= 1
            if recoil_guard != 0:
                recoil_guard -= 1
            if recoil_vas != 0:
                recoil_vas -= 1
            if recoil_blood != 0:
                recoil_blood -= 1
            person_move = 1
            number_move += 1
    else:
        print(' \nХодит босс')
        if active_smoke == 1:
            print('Из-за дымовой шашки, Босс теряет героя из виду, ненанося ему урона')
            heal_hero -= 0
            count_active_smoke -= 1
        else:
            if active_def == 1:
                def_hero += (def_hero / 2)
                count_active_def -= 1
                print('На герое есть активный баф защиты')
                print('Босс наносит урон:', atack_boss - def_hero, 'единиц')
                heal_hero -= atack_boss - def_hero
            else:
                print('Босс наносит урон:', atack_boss, 'единиц')
                heal_hero -= atack_boss
        if active_vas == 1:
            print('Василиск наносит пассивный урон боссу в размере 40 ед.')
            heal_boss -= 40
            count_active_vas -= 1
        if active_help == 1:
            print('Действует эффект пассивного лечения на герое: +20 ед. здоровья')
            heal_hero += 20
            count_active_help -= 1
        if active_blood == 1:
            print('Действует эффект кровотечения, босс теряет:', (atack_hero / 2), 'ед. здоровья')
            heal_boss -= (atack_hero / 2)
            count_active_blood -= 1
        PrintHeal()
        if active_sigh == 1 and heal_hero <= 0:
            print('Босс впал в ярость и убил вас, однако, Вы, заранее выпили зелье и оно вас воскресило')
            heal_hero = 31
            PrintHeal()
        elif active_sigh == 0 and heal_hero <= 0:
            print('Босс впал в ярость и убил вас, жаль, что Вы не успели выпить зелье возрождения')
        if recoil_smoke != 0:
            recoil_smoke -= 1
        if recoil_guard != 0:
            recoil_guard -= 1
        if recoil_vas != 0:
            recoil_vas -= 1

        if count_active_vas == 0:
            active_vas = 0
        if count_active_help == 0:
            active_help = 0
        if count_active_smoke == 0:
            active_smoke = 0
        if count_active_blood == 0:
            active_blood = 0
        if count_active_def == 0:
            active_def = 0

        if heal_boss <= 0:
            print('\nБосс побежден, игра закончена')
            break
        if heal_hero <= 0:
            print('\nГерой погиб, игра закончена')
            break

        person_move = 0
        number_move += 1

