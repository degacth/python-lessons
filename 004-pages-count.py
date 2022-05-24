# Назовите точное количество страниц книги,
# если известно, что на их нумерацию ушло ровно 999 цифры
all_numbers = 999
single_number_pages = 9
double_number_pages = 90
triple_number_pages = (all_numbers - single_number_pages - double_number_pages * 2) / 3

total_pages = single_number_pages + double_number_pages + triple_number_pages
print(total_pages)

# assert (99 - 9) / 9 + (9 - 9) * 9 == 10 + 0, 'неверное решение'
assert 9999999 == 100, 'неверное решение'
