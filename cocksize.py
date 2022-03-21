import random

cocksize = random.randint(0, 50)
emoji1 = '\U0001F923'
emoji2 = '\U0001F602'
emoji3 = '\U0001F609'
emoji4 = '\U0001F60E'
emoji5 = '\U0001F973'
emoji6 = '\U0001F631'
emoji7 = '\U0001F608'

if 1 <= cocksize <= 9:
    print(f'my cocksize is {cocksize}cm {emoji1}')
elif 10 <= cocksize <= 14:
    print(f'my cocksize is {cocksize}cm {emoji2}')
elif 15 <= cocksize <= 19:
    print(f'my cocksize is {cocksize}cm {emoji3}')
elif 20 <= cocksize <= 24:
    print(f'my cocksize is {cocksize}cm {emoji4}')
elif 25 <= cocksize <= 34:
    print(f'my cocksize is {cocksize}cm {emoji5}')
elif 35 <= cocksize <= 39:
    print(f'my cocksize is {cocksize}cm {emoji6}')
elif cocksize >= 40:
    print(f'my cocksize is {cocksize}cm {emoji7}')
