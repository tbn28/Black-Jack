import random

deck = list(('2','3','4','5','6','7','8','9','10','J','Q','K','A') * 4)
random.shuffle(deck)
value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
player = [deck.pop() for _ in range(2)]
cpu = [deck.pop() for _ in range(2)]

def check(who, hand):
    m = map(value.get, hand)

    try:
        s = sum(m)
        subtotal = int(s)
    except:
        print ("Error!")
        return 0

    if subtotal > 21:
        print('{} przegrywa. {}'.format(who, str(hand)))
        return 0

    if len(hand) > 4:
        print ('{} wygrywa. {}'.format(who, str(hand)))
        return 0

    total = [item for item in
        [subtotal] + [item for item in
         range(subtotal + 10, subtotal + 10 * hand.count('A') + 1, 10)]
         if item <= 21]

    if 21 in total:
        print ('{} wygrywa. {}'.format(who, str(hand)))
        return 0

    return total

while 1:
    pl = check('Gracz', player)
    cp = check('Komputer', cpu)

    if not pl or not cp:
        break
    print(str(player))

    while 1:
        p = input('Chcesz dobrac karte? ')
        if p.lower() == "tak":
            player.append(deck.pop())
            p = True
            break
        if p.lower() == "nie":
            p = False
            break

    ai = cp[-1] < 15

    if ai:
        cpu.append(deck.pop())

    if not p and not ai:
        if pl[-1] > cp[-1]:
            print ('Gracz wygrywa')
        elif pl[-1] < cp[-1]:
            print ('Komputer wygrywa')
        else:
            print ('Remis ')

        print('Gracz', str(player))
        print('Komputer', str(cpu))
        break