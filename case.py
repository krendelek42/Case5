"""Case-study #4 Парсинг web-страниц
Разработчики:
Докукина К.А.  Назирова Е.С.

"""

with open('input.txt', 'r') as f_in:
    with open('output.txt', 'w') as out_f:
        import urllib.request
        for line in f_in:
            url = line[0:-2]
            f = urllib.request.urlopen(url)
            s = f.read()
            text = str(s)
            part_name = text.find("nfl-c-player-header__title")
            name = text[text.find('>', part_name) + 1:text.find('</h1', part_name)]

            part_COMP = text.find('passingCompletions')
            COMP = text[text.find('>', part_COMP) + 25:text.find('<', part_COMP) - 22]

            part_ATT = text.find('passingAttempts')
            ATT = text[text.find('>', part_ATT) + 25:text.find('<', part_ATT) - 22]

            part_YDS = text.find('passingYards')
            YDS = text[text.find('>', part_YDS) + 25:text.find('<', part_YDS) - 22]

            part_TD = text.find('passingTouchdowns')
            TD = text[text.find('>', part_TD) + 25:text.find('<', part_TD) - 22]

            part_INT = text.find('passingInterceptions')
            INT = text[text.find('>', part_INT) + 25:text.find('<', part_INT) - 22]

            part_PR = text.find('passingPasserRating')
            PR = text[text.find('>', part_PR) + 25:text.find('<', part_PR) - 22]

            print(name, COMP, ATT, YDS, TD, INT, PR, file = out_f)