monsters = {}

room_dir = 'modules/adventure/room/'

dungeon = [f[:-3] for f in os.listdir(room_dir + 'dungeon') if f.endswith('.py')]

for plugin in dungeon:
    try:
        exec(open(room_dir + 'dungeon/' + plugin + ".py" , encoding='utf-8').read())
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)

#Легкие в лесу
monsters['wolf'] = {
    'name' : 'Волк',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]], ['resource', 'leather', [1,2]] ]
}



monsters['boar'] = {
    'name' : 'Кабан',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]], ['resource', 'leather', [1,2]] ]
}

monsters['skeleton_easy'] = {
    'name' : 'Скелет',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]] ]
}


#Средние в лесу
monsters['skeleton_medium'] = {
    'name' : 'Скелет',
    'level': 'medium',
    'gold' : [15,30],
    'diamond' : [1,2],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['gremolata'] = {
    'name' : 'Оживший Ветер',
    'level': 'medium',
    'gold' : [15,30],
    'diamond' : [1,2],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['boar_medium'] = {
    'name' : 'Кабан',
    'level': 'medium',
    'gold' : [15,30],
    'diamond' : [1,2],
    'loot' : [ ['resource', 'bone', [1,2]], ['resource', 'leather', [1,2]] ]
}

monsters['hedgehog'] = {
    'name' : 'Злой ёж',
    'level': 'medium',
    'gold' : [15,30],
    'diamond' : [1,2],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

#Сложные лес
monsters['duck'] = {
    'name' : 'Утка',
    'level': 'hard',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : [ ['resource', 'bone', [1,2]], ['resource', 'leather', [1,2]] ]
}

monsters['youngtree'] = {
    'name' : 'Молодой Древень',
    'level': 'hard',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : None
}


#Горы легкие
monsters['mountgoat'] = {
    'name' : 'Горный Козёл',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['cavewolf'] = {
    'name' : 'Пещерный Медведь',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['tiger'] = {
    'name' : 'Саблезубый тигр',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['Crotonyl'] = {
    'name' : 'КротоКрыл',
    'level': 'easy',
    'gold' : [10,20],
    'diamond' : False,
    'loot' : [ ['resource', 'bone', [1,2]] ]
}


#Горы средний
monsters['harpy'] = {
    'name' : 'Гарпия',
    'level': 'medium',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['poitwiw'] = {
    'name' : 'Ядовитая Виверна',
    'level': 'medium',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['sylph'] = {
    'name' : 'Сильфида',
    'level': 'medium',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : [ ['resource', 'bone', [1,2]] ]
}

monsters['revivedore'] = {
    'name' : 'Ожившая Руда',
    'level': 'medium',
    'gold' : [35,45],
    'diamond' : [1,3],
    'loot' : None
}


#Горы Сложный
monsters['stonegiant'] = {
    'name' : 'Каменный Гигант',
    'level': 'hard',
    'gold' : [30,50],
    'diamond' : [1,2],
    'loot' : [ ['resource', 'stone', [1,2]] ]
}

monsters['knight'] = {
    'name' : 'Рыцарь',
    'level': 'hard',
    'gold' : [30,50],
    'diamond' : [1,2],
    'loot' : [ ['body', '3'], ['legs', '3'], ['head', '3'], ['mask', '3'], ['gun', '5'] ]
}




monsters['Mummy'] = {
    'name' : 'Мумия',
    'level': 'hard',
    'gold' : [40,50],
    'diamond' : False,
    'loot' : False
}

monsters['Scorpio'] = {
    'name' : 'Скорпион',
    'level': 'hard',
    'gold' : [40,50],
    'diamond' : False,
    'loot' : False
}

monsters['Camel'] = {
    'name' : 'Верблюд',
    'level': 'hard',
    'gold' : [40,50],
    'diamond' : False,
    'loot' : False
}
