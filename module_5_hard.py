from time import sleep

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль в хешированном виде, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class UrTube:
    """
    Класс платформы для видео, содержащий атрибуты: список объектов User, список объектов Video,
    текущий пользователь User
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password, age):                  #метод входа в аккаунт
        for i in range(0, len(self.users)):
            if nickname == self.users[i].nickname:
                if hash(password) == self.users[i].password:
                    self.current_user = self.users[i]

    def register(self, nickname, password, age):                #метод регистрации
        for i in range(0, len(self.users)):
            if nickname == self.users[i].nickname:
                print(f'Пользователь {nickname} уже существует')
                break
        else:
            nickname = User(nickname, password, age)
            self.users.append(nickname)
            self.current_user = nickname

    def log_out(self):                                          #метод выхода из аккаунта
       self.current_user = None

    def add(self, *args):                                       #метод добавления видео
        for i in range(0, len(args)):
            self.videos.append(args[i])

    def get_videos(self, str):                                  #метод поиска названия видео
        title = []
        for i in range(0, len(self.videos)):
            if str.lower() in self.videos[i].title.lower():
                title.append(self.videos[i].title)
                continue
        return title

    def watch_video(self, str):                                 #метод воспроизведения видео
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for i in range(0, len(self.videos)):
                if str == self.videos[i].title:
                    if self.videos[i].adult_mode == True and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for self.videos[i].time_now in range(self.videos[i].time_now, self.videos[i].duration + 1):
                            print(self.videos[i].time_now)
                            sleep(1)
                        print('Конец видео')
                        self.videos[i].time_now = 0

class Video:
    """
    Класс видео, содержащий атрибуты: заголовок, продолжительность, секунда остановки, ограничение по возрасту
    """
    def __init__(self, title, duration, **args):
        self.title = title
        self.duration = duration
        self.time_now = 0
        if args.get('adult_mode') is True:
            self.adult_mode = True
        else:
            self.adult_mode = False

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

# Проверка входа в другой аккаунт методом log_in
#ur.log_in('vasya_pupkin', 'lolkekcheburek', 13)

# Т.к. в current_user находится ссылка на объект класса User, чтобы вывести его имя,
# нужно обратиться к атрибуту nickname
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')