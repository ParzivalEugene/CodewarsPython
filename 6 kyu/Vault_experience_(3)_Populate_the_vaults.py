def populate_my_vault(dwellers_count):
    overseers = 0 if not dwellers_count else 1 if 0 < dwellers_count < 51 else 2
    if overseers < 2:
        women = 0 if dwellers_count == 1 else dwellers_count // 2 if not dwellers_count % 2 else dwellers_count // 2 + 1
    else:
        women = dwellers_count // 2 - 1 if not dwellers_count % 2 else dwellers_count // 2
    men = dwellers_count - overseers - women
    return overseers, women, men


# print(populate_my_vault(0), (0, 0, 0))
# print(populate_my_vault(1), (1, 0, 0))
# print(populate_my_vault(2), (1, 1, 0))
# print(populate_my_vault(3), (1, 2, 0))
# print(populate_my_vault(4), (1, 2, 1))
# print(populate_my_vault(5), (1, 3, 1))
# print(populate_my_vault(10), (1, 5, 4))
# print(populate_my_vault(11), (1, 6, 4))
# print(populate_my_vault(23), (1, 12, 10))
# print(populate_my_vault(50), (1, 25, 24))
# print(populate_my_vault(51), (2, 25, 24))
# print(populate_my_vault(200), (2, 99, 99))
