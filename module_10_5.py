from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == "__main__":

    filenames = [f'file_{number}.txt' for number in range(1, 5)]

    start_1 = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_1 = datetime.now()
    print(f"{end_1 - start_1} (линейное выполнение)")

    start_2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(f"{end_2 - start_2} (многопроцессное выполнение)")
