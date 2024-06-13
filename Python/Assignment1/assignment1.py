# Assignment 1 - Parking (a) Lot

# Name: 
# Time needed for solution: 


def load_parking_records(file_path):  # 0.75b

    records = []
    with open(file_path) as f:
        for line in f:
            line = line.replace("\n", "")
            data = line.strip().split(",")
            p = data[:1]
            for value in data[1:]:
                p.append(int(value))
            records.append(tuple(p))
    return records


def load_prices(file_path):  # 0.75b

    prices = {}
    with open(file_path) as f:
        for line in f:
            data = line.strip().split(":")
            prices[data[0]] = float(data[1])

    return prices


def calculate_parking_time(start_h, start_m, end_h, end_m):  # 0.5b

    start = start_h * 60 + start_m
    end = end_h * 60 + end_m
    return end - start


def get_parking_fee(time_in_minutes, prices):  # 1b

    hours = time_in_minutes // 60
    ticket = ["3h", "6h", "1d"]
    p = 0.0
    n = -1
    if time_in_minutes < 15:
        p = 0.0
    elif time_in_minutes >= 15 and time_in_minutes < 30:
        p = prices["30m"]
    elif time_in_minutes >= 30 and time_in_minutes <= 60:
        p = prices["1h"]
    elif time_in_minutes > 60 and time_in_minutes <= 180:
        p = prices["h+"] * hours + prices["1h"]
        n = 0
    elif time_in_minutes > 180 and time_in_minutes <= 360:
        p = prices["h+"] * (hours-2) + prices["3h"]
        n = 1
    elif time_in_minutes > 360 and time_in_minutes <= 1440:
        p = prices["h+"] * (hours - 5) + prices["6h"]
        n = 2

    if n >= 0:
        if prices[ticket[n]] < p:
            return prices[ticket[n]]
    
    return p
    
    

def calculate_average_parking_fee(records, prices):  # 0.5b
    count = 0
    total = 0
    for r in records:
        time = calculate_parking_time(r[1], r[2], r[3], r[4])
        total += get_parking_fee(time, prices)
        count += 1
    
    return total / count


def calculate_average_parking_time(records):  # 0.5b
    time = 0
    count = 0
    for r in records:
        time += calculate_parking_time(r[1], r[2], r[3], r[4])
        count += 1

    return time / count



def calculate_average_stays(records):  # 0.5b
    car = []
    for r in records:
        if r[0] not in car:
            car.append(r[0])
    if len(car) > 0:
        return len(records) / len(car)
    return 0

def get_most_common_region(records):  # 1b
    dist_code = {}
    for r in records:
        if r[0][:2] not in dist_code:
            dist_code[r[0][:2]] = 0
        dist_code[r[0][:2]] += 1
    
    m = max(dist_code.values())
    for region, occurence in dist_code.items():
        if occurence == m:
            return region


def get_busiest_hour(records):  # 0.5b
    cars = []
    car_count = {}
    opening_hour = 23
    closing_hour = 0
    count = 0
    
    for r in records:
        cars.append((r[1], r[3]))
        if r[1] < opening_hour:
            opening_hour = r[1]
        if r[3] > closing_hour:
            closing_hour = r[3]

    for hour in range(opening_hour, closing_hour + 1):
        for time in cars:
            if hour == time[0]:
                count += 1
            if hour == time[1] + 1:
                count -= 1
        car_count[hour] = count
    
    m = max(car_count.values())
    for time in car_count:
        if car_count[time] == m:
            return time


def get_max_number_of_cars(records):  # 2b

    car_times = []
    
    for r in records:
        car_times.append((r[1]*60 + r[2], r[3]* 60 + r[4]))
    
    open = records[0][1]*60
    close = car_times[0][1]
    
    for time in car_times:
        if time[1] > close:
            close = time[1]
    
    list_cars_per_min = []
    car_count_per_min = 0
    
    for min in range(open, close):
        for time in car_times:
            if min == time[0]: 
                car_count_per_min += 1
            if min == time[1]:
                car_count_per_min -= 1
        list_cars_per_min.append(car_count_per_min)
        

    return max(list_cars_per_min), list_cars_per_min


def optimize_hourly_fee(records, prices): # 2b
    max_revenue = 0
    opt_fee = 0
    for fee in range(int(prices['30m'] * 10 + 1), int(prices['1h'] * 10)):
        fee /= 10
        revenue = 0
        for record in records:
            duration = calculate_parking_time(record[1], record[2], record[3], record[4])
            if duration <= 30:
                revenue += prices['30m']
            elif duration <= 60:
                revenue += prices['1h']
            else:
                hours = duration // 60
                mins = duration % 60
                revenue += prices['1h'] * (hours - 1) + prices['h+'] * (hours - 1)
                if mins > 30:
                    revenue += prices['1h']
                else:
                    revenue += prices['30m']
                if hours > 1:
                    revenue += fee * (hours - 1)
        if revenue > max_revenue:
            max_revenue = revenue
            opt_fee = fee
    return opt_fee


if __name__ == '__main__':
    records = load_parking_records("./samples/parking_logs_01.csv")
    prices = load_prices("./samples/prices_01.txt")
    # print(calculate_parking_time(7, 45, 11, 23))
    # print(get_parking_fee(145, {'30m': 1.5, '1h': 3.0, '3h': 7.5, '6h': 12.0, '1d': 24.0, 'h+': 2.5}))
    # records = load_parking_records("./samples/parking_logs_01.csv")
    # print(get_most_common_region(records))
    # print(get_busiest_hour(records))
    # print(get_max_number_of_cars(records))