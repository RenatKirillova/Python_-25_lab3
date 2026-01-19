# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, send_group, separator = ","):
    result = []

    first_list = first_group.split(separator)
    second_list = send_group.split(separator)
    for person in first_list:
        if person in second_list:
            result.append(person)
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, separator = "|" ))
# TODO Провеьте работу функции с разделителем отличным от запятой
