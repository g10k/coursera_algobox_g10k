
def find_fuelfills_greedy_algorithm(fuelfill_station_list: list, fuel_tank:int):
    """ Ищем пувть с минимальным количеством остановок На каждой заправке заправляем полный бак

    :param fuelfill_station_list: список из расстояния от следующей заправки до предыдущей, первое число -0
    :param fuel_tank: - вместимость бака.
    :return:
    """

    result = [0]
    finish_trip = False
    while not finish_trip:
        next_fuel = fuel_tank
        next_fuel_choosen = False
        last_fuel_index = result[-1]
        for j, next_fuel_station in enumerate(fuelfill_station_list[last_fuel_index+1:]):
            if next_fuel - next_fuel_station <= 0:
                next_fuel_choosen = True
            else:
                next_fuel -= next_fuel_station
            if next_fuel_choosen:
                result.append(j+last_fuel_index)
                break
        if sum(fuelfill_station_list[result[-1]:]) < fuel_tank:
            finish_trip = True
    return result


if __name__ == '__main__':
    res = find_fuelfills_greedy_algorithm([0,4,3,2,6,3,2,4], 8.5)
    print(res)