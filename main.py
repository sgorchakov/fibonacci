import sys


def read_lines_from_file(file_name):
    lines = []
    try:
        with open(file_name, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    lines.append(line)
                else:
                    continue
    except FileNotFoundError:
        print('Указанный файл не найден')
    return lines


def write_line_in_file(line):
    try:
        with open('output.txt', 'a') as file:
            file.write(str(line))
    except Exception:
        print('Данные не могут быть записаны. Ошибка доступа к файлу')


def fibonacci(element_number):
    left_number = 0
    right_number = 1
    i = 1
    while i <= element_number.__len__() - 1:
        fib = left_number + right_number
        for element_of_list in element_number:
            sub_list = element_of_list.split(' ')
            if str(fib) in sub_list:
                revers_count = element_of_list.__len__() - 1
                line_for_convert = list(element_of_list)
                revers_line = ''
                while revers_count >= 0:
                    revers_line = revers_line + line_for_convert[revers_count]
                    revers_count -= 1
                write_line_in_file(revers_line + '\n')
        left_number = right_number
        right_number = fib
        i += 1


if __name__ == '__main__':
    file_path = 'source.txt'
    if sys.argv.__len__() > 1:
        file_path = sys.argv[1]
    fibonacci(read_lines_from_file(file_path))
