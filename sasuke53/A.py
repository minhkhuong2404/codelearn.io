def who_would_win(cat_a, mouse, cat_b):
    dis_a = abs(cat_a - mouse)
    dis_b = abs(cat_b - mouse)
    if dis_a > dis_b:
        return "Cat B"
    elif dis_a < dis_b:
        return "Cat A"
    else:
        return "The mouse has escaped"
