import main
import pytest


def test_everything():
    result = main.count_reward(100000, 10, 4.1)
    assert 20000 == result


@pytest.mark.parametrize(
    "wage, level, preview, expectation",
    [
        (69999, 11, 3, "Wage out of range"),
        (750001, 11, 3, "Wage out of range"),
        (100000, 6, 3, "Level out of range"),
        (100000, 16, 3, "Level out of range"),
        (100000, 11, 0, "PR out of range"),
        (100000, 11, 6, "PR out of range"),
    ]
)
def test_number(wage, lvl, preview, expectation):
    with pytest.raises(ValueError, match=expectation):
        main.count_reward(wage, lvl, preview)


def test_data():
    with pytest.raises(TypeError, match="Incorrect format"):
        main.count_reward("asdf", 10, 5)


@pytest.mark.parametrize(
    "wage, lvl, preview",
    [
        (None, 10, 4),
        (75000, None, 4),
        (75000, 10, None),
    ]
)
def test_null(wage, lvl, preview):
    with pytest.raises(main.NullAgrumentException, match="Входной параметр определён"):
        main.count_reward(wage=wage, lvl=lvl, preview=preview)


"""Границы по уровню"""
preset_lvl_borders = [6, 7, 17, 18]
"""Границы по PR"""
preset_preview_borders = [0.9, 1, 5, 5.1]
"""Гранцы по зарплате"""
preset_wage_borders = [69900, 70000, 750000, 751000]
"""Наибольшая премия"""
max_res = 300000
"""Наименьшая премия"""
min_res = 0


@pytest.mark.parametrize(["wage", "lvl", "preview"], [values for values in
                                                             AllPairs([preset_wage_borders,
                                                                       preset_lvl_borders,
                                                                       preset_preview_borders])])
def test_count_reward(wage, lvl, preview):
    try:
        with pytest.raises(ValueError) as exc:
            result = main.count_reward(wage=wage, lvl=lvl, preview=preview)
        assert str(exc.value) in ["Зарплата не соответствует диапазону",
                                  "Недопустимый уровень инженера",
                                  "Неверное значение Performance Review"]
    except _pytest.outcomes.Failed:
        assert min_res < result < max_res
