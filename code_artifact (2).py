"""
Автоматические модульные тесты для проверки чистоты,
неизменяемости и рекурсии.
"""

import unittest
from core import (
    validate_score,
    calculate_average,
    calculate_median,
    determine_admission_status,
    transform_scores,
    filter_scores,
    recursive_max,
    build_student_report
)


class TestFunctionalCore(unittest.TestCase):
    
    def test_immutability_of_source_data(self):
        """Проверка неизменяемости входного списка."""
        source = [70, 80, 90]
        snapshot = source.copy()
        build_student_report("Test Student", source)
        self.assertEqual(source, snapshot, "Исходный список не должен изменяться!")

    def test_valid_scores_calculation(self):
        """Проверка правильности расчёта характеристик."""
        scores = [60.0, 70.0, 80.0]
        self.assertEqual(calculate_average(scores), 70.0)
        self.assertEqual(calculate_median(scores), 70.0)
        self.assertEqual(recursive_max(scores), 80.0)

    def test_admission_status_logic(self):
        """Проверка статусов допуска."""
        self.assertEqual(determine_admission_status(55.0), "допущен")
        self.assertEqual(determine_admission_status(45.0), "не допущен")
        self.assertEqual(determine_admission_status(None), "нет данных")

    def test_recursive_max_empty_raises_value_error(self):
        """Проверка вызова ошибки рекурсивным максимумом на пустом списке."""
        with self.assertRaisesRegex(ValueError, "пуста"):
            recursive_max([])

    def test_invalid_type_raises_type_error(self):
        """Проверка отклонения некорректных типов (включая bool)."""
        with self.assertRaises(TypeError):
            validate_score("восемьдесят")
        with self.assertRaises(TypeError):
            validate_score(True)

    def test_out_of_range_raises_value_error(self):
        """Проверка отклонения чисел вне диапазона [0, 100]."""
        with self.assertRaises(ValueError):
            validate_score(105)
        with self.assertRaises(ValueError):
            validate_score(-5)

    def test_higher_order_functions(self):
        """Проверка функций высшего порядка."""
        scores = [40.0, 60.0, 80.0]
        bonus_scores = transform_scores(scores, lambda x: min(100.0, x + 10))
        self.assertEqual(bonus_scores, [50.0, 70.0, 90.0])
        
        passed_scores = filter_scores(scores, lambda x: x >= 50)
        self.assertEqual(passed_scores, [60.0, 80.0])

    def test_deterministic_behavior(self):
        """Проверка детерминированности результата."""
        data = [50.0, 75.0, 100.0]
        rep1 = build_student_report("Amina", data)
        rep2 = build_student_report("Amina", data)
        self.assertEqual(rep1, rep2)


if __name__ == "__main__":
    unittest.main()