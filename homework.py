class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type,                 
                 duration,
                 distance,
                 speed,
                 calories
                 ) -> None:
        
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        
    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; '
                f'Ср. скорость: {self.speed} км/ч; '
                f'Потрачено ккал: {self.calories}.')    


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_IN_H = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:

        self.action = action
        self.duration = duration
        self.weight = weight
        pass

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(Training,
                           self.duration,
                           self.get_distance,
                           self.get_mean_speed,
                           self.get_spent_calories
                           )


class Running(Training):
    """Тренировка: бег."""

    LEN_STEP = 0.65
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float) -> None:

        super().__init__(action,
                         duration,
                         weight)

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER * self.get_distance()
                + self.CALORIES_MEAN_SPEED_SHIFT) * self.weight
                / self.weight / self.M_IN_KM * self.duration)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    WEIGHT_MODIFICATOR = 0.035
    SPEED_MODIFICATOR = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:

        super().__init__(action,
                         duration,
                         weight)

        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.WEIGHT_MODIFICATOR * self.weight
                 + (self.get_mean_speed() ** 2 / self.height )
                 * self.SPEED_MODIFICATOR * self.weight)
                * (self.duration * self.MIN_IN_H))


class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38
    CALORY_BURN_MODIFICATOR = 2
    SWIMM_SPEED_SHIFT = 1.1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int) -> None:

        super().__init__(action,
                         duration,
                         weight)

        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return (self.length_pool * self.count_pool / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.SWIMM_SPEED_SHIFT)
                * self.CALORY_BURN_MODIFICATOR * self.weight
                * self.duration)


training_type: dict = {'SWM': Swimming,
                           'RUN': Running,
                           'WLK': SportsWalking}

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    
    while True:
        activity: Training = training_type[workout_type](*data)

        break

    return activity
    

def main(training: Training) -> None:
    """Главная функция."""
    
    info = training.show_training_info()

    return print(f'{info.get_message}')


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
