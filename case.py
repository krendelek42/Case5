"""Case-study #4 Парсинг web-страниц
Разработчики:
Докукина К.А. 60%  Назирова Е.С. 40%

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
            COMP = int(text[text.find('>', part_COMP) + 25:text.find('<', part_COMP) - 22])

            part_ATT = text.find('passingAttempts')
            ATT = int(text[text.find('>', part_ATT) + 25:text.find('<', part_ATT) - 22])

            part_YDS = text.find('passingYards')
            YDS = int(text[text.find('>', part_YDS) + 25:text.find('<', part_YDS) - 22])

            part_TD = text.find('passingTouchdowns')
            TD = int(text[text.find('>', part_TD) + 25:text.find('<', part_TD) - 22])

            part_INT = text.find('passingInterceptions')
            INT = int(text[text.find('>', part_INT) + 25:text.find('<', part_INT) - 22])

            part_PR = text.find('passingPasserRating')
            PR = float(text[text.find('>', part_PR) + 25:text.find('<', part_PR) - 22])

            out_f.writelines('{0:<20} {1:<7} {2:<7} {3:<7} {4:<7} {5:<7} {6:<7.2f}\n'.format(name, COMP, ATT, YDS, TD, INT, PR))
