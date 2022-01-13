import decimal


def count_lvl_mod(lvl: int) -> decimal:
    if lvl < 10:
        lvl_reward = 0.05
    elif 10 <= lvl < 13:
        lvl_reward = 0.1
    elif 13 <= lvl < 15:
        lvl_reward = 0.15
    else:
        lvl_reward = 0.2
    return lvl_reward


def count_p_mod(preview: int):
    if 2 <= preview < 2.5:
        p_reward = 0.25
    elif 2.5 <= preview < 3:
        p_reward = 0.5
    elif 3 <= preview < 3.5:
        p_reward = 1
    elif 3.5 <= preview < 4:
        p_reward = 1.5
    else:
        p_reward = 2
    return p_reward


def count_reward(wage: int, lvl: int, preview: decimal) -> float:
    if wage is None or lvl is None or preview is None:
        raise NullAgrumentException("Входной параметр не определён")
    if not isinstance(wage, int) or not isinstance(lvl, int):
        raise TypeError("Некорректный формат данных")
    if wage < 70000 or 750000 < wage:
        raise ValueError("Значение зарплаты не входит в диапазон")
    if lvl < 7 or 15 < lvl:
        raise ValueError("Уровень инженера не входит в диапазон")
    if preview < 1 or 5 < preview:
        raise ValueError("Оценка PR не входит в диапазон")
    lvl_mod = count_lvl_mod(lvl)
    p_mod = count_p_mod(preview)

    reward = wage * lvl_mod * p_mod
    return reward


class NullAgrumentException(Exception):
    pass
