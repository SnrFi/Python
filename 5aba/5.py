import random

def get_valid_input():
    while True:
        try:
            stones = int(input("Сколько камней вы берёте (1, 2 или 3)? "))
            if stones in [1, 2, 3]:
                return stones
            else:
                print("Ошибка! Можно брать только 1, 2 или 3 камня.")
        except ValueError:
            print("Ошибка! Введите число 1, 2 или 3.")

def computer_move(remaining_stones):
    if remaining_stones > 3:
        return random.randint(1, 3)
    return remaining_stones

def main():
    print("Добро пожаловать в игру 'Камни'!")
    print("Правила: Игроки по очереди берут 1, 2 или 3 камня. Побеждает тот, кто возьмёт последний камень.\n")

    # Инициализация количества камней
    total_stones = random.randint(4, 30)
    print(f"На столе {total_stones} камней.")

    # Основной цикл игры
    while total_stones > 0:
        # Ход пользователя
        user_stones = get_valid_input()
        total_stones -= user_stones
        print(f"Вы взяли {user_stones} камней. Осталось {total_stones} камней.")
        if total_stones == 0:
            print("Поздравляем! Вы выиграли!")
            break

        # Ход компьютера
        comp_stones = computer_move(total_stones)
        total_stones -= comp_stones
        print(f"Компьютер взял {comp_stones} камней. Осталось {total_stones} камней.")
        if total_stones == 0:
            print("Компьютер выиграл! Удачи в следующий раз.")
            break
print()
main()
