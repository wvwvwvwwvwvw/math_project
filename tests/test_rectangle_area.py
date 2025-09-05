import pytest
from app.geometry.rectangle_area import rectangle_area

def test_rectangle_area_correct_lenght():
    """
    Проверка целых положительных значений длин сторон прямоугольника
    :return:
    """

    #arrange
    width = "3"
    height = "5" 
    expected_result = 15
    #act
    actual_result = rectangle_area(width, height)   
    #assert
    assert actual_result == pytest.approx(expected_result)


    def test_rectangle_area_string_data():
        """
        Тестирование вычисления площади со строкой в качестве стороны прямоугольника
        """

        #arrange
        width = "hello"
        height = "5.2"
        #act
        with pytest.raises(ValueError) as exc_info:
            rectangle_area(width, height)

        #assert
        assert str(exc_info.value) == "Введено не числовое значение стороны"