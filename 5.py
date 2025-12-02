def process_list(input_list):
    assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
    print(f"Список містить {len(input_list)} елемента\ів)")
def get_user_list():
    user_input = input("Введіть елементи: ")
    user_list = [item.strip() for item in user_input.split(',')]
    return user_list
try:
    my_list = get_user_list()
    process_list(my_list)
except AssertionError as e:
    print(f"Помилка: {e}")
except ValueError:
    print("Помилка вводу. Будь ласка, введіть елементи коректно.")
