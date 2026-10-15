"""
Императивная оболочка приложения.
Отвечает за ввод, вывод и запуск программы.
"""

from core import build_student_report


def main():
    raw_data = [65, 80, 45, 95, 70]
    print("=== Демонстрация работы функционального ядра ===")
    print(f"Исходные данные: {raw_data}")
    
    report = build_student_report("Иван Иванов", raw_data)
    
    print("\n--- Сформированный отчёт ---")
    for key, value in report.items():
        print(f"{key:<10}: {value}")


if __name__ == "__main__":
    main()