monster = {}

enabled_plugins = [f[:-3] for f in os.listdir('modules/tutorial') if f.endswith('.py')]
print ('|-----Подключение модулей обучения-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/tutorial/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)

#test
enabled_plugins = [f[:-3] for f in os.listdir('modules/shop') if f.endswith('.py')]
print ('|-----Подключение модулей магазина-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/shop/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)



enabled_plugins = [f[:-3] for f in os.listdir('modules/сraft') if f.endswith('.py')]
print ('|-----Подключение модулей craft-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/сraft/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)

enabled_plugins = [f[:-3] for f in os.listdir('modules/adventure') if f.endswith('.py')]
print ('|-----Подключение модулей приключений-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/adventure/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)

enabled_plugins = [f[:-3] for f in os.listdir('modules/city') if f.endswith('.py')]
print ('|-----Подключение модулей города-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/city/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)

enabled_plugins = [f[:-3] for f in os.listdir('modules/hero') if f.endswith('.py')]
print ('|-----Подключение модулей героя-----|')
for plugin in enabled_plugins:
    try:
        exec(open("./modules/hero/" + plugin + ".py" , encoding='utf-8').read())
        print("Подключен " + plugin)
    except Exception as e:
        print("Ошибка подключения " + plugin)
        print(e)
        exit(1)