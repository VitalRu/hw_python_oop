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

    def get_message(self):
        return print(f'Тип тренировки: {self.training_type}; '
                     f'Длительность: {self.duration} ч.; '
                     f'Дистанция: {self.distance} км; '
                     f'Ср. скорость: {self.speed} км/ч; '
                     f'Потрачено ккал: {self.calories}.'
                     )


M_IN_KM = 1000

CM_IN_M = 100

H_IN_MIN = 60

MIN_IN_S = 60


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65

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
        return self.action * self.LEN_STEP / M_IN_KM

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
                           self.get_spent_calories)


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
                / self.weight / M_IN_KM * self.duration * H_IN_MIN)


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
                 + (self.get_mean_speed() ** 2 / self.height / CM_IN_M)
                 * self.SPEED_MODIFICATOR * self.weight)
                * (self.duration * H_IN_MIN))


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
        return (self.length_pool * self.count_pool / M_IN_KM
                / (self.duration * H_IN_MIN))

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.SWIMM_SPEED_SHIFT)
                * 2 * self.weight * (self.duration * H_IN_MIN))


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
