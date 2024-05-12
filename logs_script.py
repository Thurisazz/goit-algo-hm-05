import sys
from pathlib import Path


def parse_log_line(line: str) -> dict:
    line_split = line.split()
    logs_info = {
        'Date': line_split[0],
        'Time': line_split[1],
        'Level': line_split[2],
        'Message': ' '.join(line_split[3:]).strip(),
    }
    return logs_info


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            parsed_logs = [parse_log_line(line.strip()) for line in file]
        return parsed_logs
    except FileNotFoundError:
        print('Файл не знайдено')
        sys.exit(1)
    except IOError:
        print("Помилка: Помилка відкриття/читання файлу.")
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda elem: elem['Level']== level, logs))


def count_logs_by_level(logs: list) -> dict:
    count_by_level = {}
    for log in logs:
        level = log['Level']
        count_by_level[level] = count_by_level.get(level, 0) + 1
    return count_by_level


def display_log_counts(counts: dict):
    header = '| {:^16} | {:^10} |'.format('Рівень логування', 'Кількість')
    separator = '-'*len(header)
    body = ''
    for level, count in counts.items():
        body += '| {:<16} | {:^10} |\n'.format(level, count)
    table = '\n'.join([separator, header, separator, body])
    print(table)


def display_error_logs(logs: list):
    print(f"Деталі логів для рівня '{log_level}':")
    for log in logs:
        print('{} {}: {}'.format(log['Date'], log['Time'], log['Message']))



file_path = sys.argv[1]


logs = load_logs(file_path)
counts = count_logs_by_level(logs)
result = display_log_counts(counts)

if len(sys.argv) > 2:
    log_level = sys.argv[2].upper()
    if log_level in counts:
        error_logs = filter_logs_by_level(logs, log_level)
    display_error_logs(error_logs)

