# Удалил все строчки с комментариями, чтобы flake8 не ругался

import psutil

path = "/"
# Имитируем хаотичные пробелы и плохой стиль
usage = psutil.disk_usage(path)
free_space = usage.free / (1024 * 1024 * 1024)
print("Свободно гигабайт:", free_space)
if free_space < 10:
    print("Внимание: мало места!")

# Удалил все строчки с комментариями, чтобы flake8 не ругался
