"""
Модуль функционального ядра для анализа оценок (Вариант 1).
Содержит чистые функции, неизменяемые преобразования и рекурсию.
"""

from typing import Any, Callable, Sequence, Optional, Dict


def validate_score(score: Any) -> float:
    """Проверяет один балл на корректность."""
    if isinstance(score, bool) or not isinstance(score, (int, float)):
        raise TypeError("Балл должен быть числовым значением (int или float).")
    if not (0 <= score <= 100):
        raise ValueError("Балл должен находиться в диапазоне от 0 до 100.")
    return float(score)


def validate_scores(scores: Sequence[Any]) -> list[float]:
    """Возвращает новый список валидированных оценок."""
    return [validate_score(s) for s in scores]


def calculate_average(scores: Sequence[float]) -> Optional[float]:
    """Чистая функция вычисления среднего значения."""
    if not scores:
        return None
    return sum(scores) / len(scores)


def calculate_median(scores: Sequence[float]) -> Optional[float]:
    """
    Чистая функция вычисления медианы.
    Не изменяет исходную последовательность.
    """
    if not scores:
        return None
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2
    if n % 2 == 1:
        return sorted_scores[mid]
    return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2.0


def determine_admission_status(average_score: Optional[float], threshold: float = 50.0) -> str:
    """Возвращает статус допуска к экзамену/аттестации."""
    if average_score is None:
        return "нет данных"
    return "допущен" if average_score >= threshold else "не допущен"


def transform_scores(scores: Sequence[float], operation: Callable[[float], float]) -> list[float]:
    """Применяет трансформацию к каждой оценке, возвращая новый список."""
    return [operation(s) for s in scores]


def filter_scores(scores: Sequence[float], predicate: Callable[[float], bool]) -> list[float]:
    """Отбирает оценки по условию, возвращая новый список."""
    return [s for s in scores if predicate(s)]


def recursive_max(values: Sequence[float]) -> float:
    """
    Рекурсивный поиск максимального балла.
    Базовые случаи: пустой список (ошибка) и список из 1 элемента.
    """
    if not values:
        raise ValueError("Последовательность пуста")
    if len(values) == 1:
        return values[0]
    
    tail_max = recursive_max(values[1:])
    return values[0] if values[0] > tail_max else tail_max


def build_student_report(name: str, raw_scores: Sequence[Any]) -> Dict[str, Any]:
    """Создаёт неизменяемый отчёт о студенте."""
    checked_scores = validate_scores(raw_scores)
    avg_val = calculate_average(checked_scores)
    
    return {
        "name": name.strip(),
        "scores": tuple(checked_scores),
        "average": avg_val,
        "median": calculate_median(checked_scores),
        "maximum": recursive_max(checked_scores) if checked_scores else None,
        "status": determine_admission_status(avg_val)
    }