# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

    # Пример:
    # k = 'ноутбук'
    # # 12



k = 'ноутбук'
# 12

alphabet = {
    'А, В, Е, И, Н, О, Р, С, Т, A, E, I, O, U, L, N, S, T, R': 1,
    'Д, К, Л, М, П, У, D, G': 2,
    'Б, Г, Ё, Ь, Я, B, C, M, P': 3,
    'F, H, V, W, Y, Й, Ы': 4,
    'Ж, З, Х, Ц, Ч, K': 5,
    'J, X, Ш, Э, Ю': 8,
    'Ф, Щ, Ъ, Q, Z': 10
}

def get_letter_value(search_letter, scrabble):
    found_value = None

    for key in scrabble:
        if search_letter in key:
            found_value = scrabble[key]
            break

    if found_value is not None:
        return found_value
    else:
        return None

def get_price_world(world):
    price = 0
    for letter in world:
        letter_upper = letter.upper()
        price += get_letter_value (letter_upper, alphabet)        
    return price
    
print(
    get_price_world(k)
)