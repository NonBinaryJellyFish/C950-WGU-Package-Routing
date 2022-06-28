import csv
import hashmap


class packages:

    def __init__(self):
        self.package_id = None
        self.delivery_addr = None
        self.current_loc = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.deadline = None
        self.weight = None
        self.notes = None
        self.delivery_status = None
        self.leave_time = None


truck_one_packages = []
truck_two_packages = []
truck_three_packages = []


def create_all_package_list():
    all_pkg = hashmap.hash_table()
    with open('data/WGUPS Package File.csv', encoding="utf-8-sig") as file:
        csvReader = csv.reader(file, delimiter=',')

        for _ in csvReader:
            tmp_pkg = packages()
            tmp_pkg.package_id = _[0]
            tmp_pkg.delivery_addr = _[1]
            tmp_pkg.city = _[2]
            tmp_pkg.state = _[3]
            tmp_pkg.zip_code = _[4]
            tmp_pkg.deadline = _[5]
            tmp_pkg.weight = _[6]
            tmp_pkg.notes = _[7]
            tmp_pkg.delivery_status = 'At The Hub'
            all_pkg.insert_entry(tmp_pkg.package_id, tmp_pkg)

            if '84104' in tmp_pkg.zip_code and '10:30' not in tmp_pkg.deadline:
                truck_three_packages.append(tmp_pkg)
            if tmp_pkg.deadline != 'EOD':
                truck_one_packages.append(tmp_pkg)
            if 'Can only be' or 'Delayed' in tmp_pkg.notes:
                truck_two_packages.append(tmp_pkg)
            if tmp_pkg not in truck_one_packages and tmp_pkg not in truck_two_packages and tmp_pkg not in truck_three_packages:
                if len(truck_two_packages) < len(truck_three_packages):
                    truck_two_packages.append(tmp_pkg)
                else:
                    truck_three_packages.append(tmp_pkg)
        file.close()
    return all_pkg.table


create_all_package_list()
print(truck_one_packages, '\n', truck_two_packages, '\n', truck_three_packages)