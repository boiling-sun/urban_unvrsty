"""
Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать 
методы добавления видео, авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), 
time_now(секунда остановки (изначально 0)), 
adult_mode(ограничение по возрасту, bool (False по умолчанию))

Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

Метод log_in, который принимает на вход аргументы: nickname, password и пытается 
найти пользователя в users с такими же логином и паролем. 
Если такой пользователь существует, то current_user меняется на найденного. 
Помните, что password передаётся в виде строки, а сравнивается по хэшу.

Метод register, который принимает три аргумента: nickname, password, age, 
и добавляет пользователя в список, если пользователя не существует (с таким же nickname). 
Если существует, выводит на экран: "Пользователь {nickname} уже существует". 
После регистрации, вход выполняется автоматически.

Метод log_out для сброса текущего пользователя на None.

Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, 
если с таким же названием видео ещё не существует. В противном случае ничего не происходит.

Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, 
содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' 
(не учитывать регистр).

Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), 
то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
После текущее время просмотра данного видео сбрасывается.
Для метода watch_video так же учитывайте следующие особенности:
Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. 
В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, 
т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
После воспроизведения нужно выводить: "Конец видео"
"""

from time import sleep

class User:
    """
    Атрибуты: 
        nickname (str): имя пользователя, 
        password (int): в хэшированном виде, 
        age (int): возраст.
    """

    def __init__(self, username, password, age):
        self.username = username
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        """Хэширует пароль с помощью встроенной функции."""
        return hash(password)

    def verify_password(self, password):
        """Соответствует ли хэш пароля хэшу атрибута password."""
        return self.password == self.hash_password(password)

    def __repr__(self):
        return f'User(username={self.username}, password={self.password}, age={self.age})'

    def __str__(self):
        """Возвращает username."""
        return f'{self.username}'
    
    
class Video:
    """
    Атрибуты: 
        title (str): заголовок, 
        duration (int): продолжительность (секунды), 
        time_now (int): секунда остановки (изначально 0), 
        adult_mode (bool): ограничение по возрасту (False по умолчанию)
    """
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __len__(self):
        """Возвращает duration."""
        return self.duration
    
    def __repr__(self):
        return f'Video(title={self.title}, duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode})'

    def watch(self):
        """Симулирует просмотр видео, увеличивая time_now и выводя эти значения на экрагн."""
        for _ in range(len(self)):
            self.time_now += 1
            print(f'{self.time_now}', end=' ')
            sleep(1)
        print('Конец видео')
        return


class UrTube:
    """
    Атрибуты: 
        users (list): список объектов User, 
        videos (list): список объектов Video, 
        current_user (User): текущий залогиненный пользователь
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, item):
        return any(user.username == item for user in self.users) or any(video.title == item for video in self.videos)

    def get_user_by_name_and_password(self, nickname, password):
        """Возвращет пользователя по логину и паролю, если он есть в системе"""
        if nickname in self:
            return next(user for user in self.users if user.username == nickname and user.verify_password(password))
        else:
            return None


    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается 
        найти пользователя в users с такими же логином и паролем. 
        Если такой пользователь существует, то current_user меняется на найденного. 
        Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        """
        if user := self.get_user_by_name_and_password(nickname, password):
            self.current_user = user
            print(f'Добро пожаловать в UrTube, {self.current_user}.')
        else:
            print(f'Пользователь {nickname} не найден или неверный пароль.')
        return

    def register(self, nickname, password, age):
        """
        Добавляет пользователя в список, если пользователя не существует (с таким же nickname). 
        После регистрации, вход выполняется автоматически.
        """
        if nickname in self:
            print(f'Пользователь {nickname} уже существует.')
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f'Пользователь {nickname} успешно зарегистрирован.')
        self.current_user = new_user
        return

    def log_out(self):
        """Метод log_out для сброса текущего пользователя на None."""
        print(f'До свидания, {self.current_user}.')
        self.current_user = None
        return

    def add(self, *videos):
        """
        Принимает неограниченное кол-во объектов класса Video и все добавляет в videos, 
        если с таким же названием видео ещё не существует.
        """
        for video in videos:
            if video.title not in self:
                self.videos.append(video)
        return
    
    def get_videos(self, word):
        """
        Принимает поисковое слово и возвращает список названий всех видео, 
        содержащих поисковое слово (не учитывает регистр).
        """
        return [video.title for video in self.videos if word.lower() in video.title.lower()]
    
    def get_video_by_title(self, title):
        """
        Метод принимает название видео и возвращает объект класса Video, 
        если не находит точного совпадения(вплоть до пробела), то возвращает None.
        """
        if title in self:
            return next(video for video in self.videos if title == video.title)
        else:
            return None

    def watch_video(self, title):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), 
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. 
        После текущее время просмотра данного видео сбрасывается.
        Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. 
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, 
        т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста, покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        """
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        if video := self.get_video_by_title(title):
            if video.adult_mode and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                return
            video.watch()
        else:
            print(f'Видео "{title}" не найдено.')
            return

    
def main():
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший')) # ['Лучший язык программирования 2024 года']
    print(ur.get_videos('ПРОГ')) # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?') # Войдите в аккаунт, чтобы смотреть видео
    ur.register('vasya_pupkin', 'foobarbaz', 13) # Пользователь vasya_pupkin успешно зарегистрирован.
    ur.watch_video('Для чего девушкам парень программист?') # Вам нет 18 лет, пожалуйста, покиньте страницу
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25) # Пользователь urban_pythonist успешно зарегистрирован.
    
    ur.log_in('vasya_pupkin', 'foobarbaz') # Добро пожаловать в UrTube, vasya_pupkin.
    ur.watch_video('Для чего девушкам парень программист?') # Вам нет 18 лет, пожалуйста, покиньте страницу
    ur.log_out() # До свидания, vasya_pupkin.
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF') # Добро пожаловать в UrTube, urban_pythonist.
    ur.watch_video('Для чего девушкам парень программист?') # 1 2 3 4 5 6 7 8 9 10 Конец видео

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55) # Пользователь vasya_pupkin уже существует.
    print(ur.current_user) # urban_pythonist

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!') # Видео "Лучший язык программирования 2024 года!" не найдено.


if __name__ == '__main__':
    main()
