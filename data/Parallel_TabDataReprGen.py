from TabDataReprGen import main
from multiprocessing import Pool

# number of files to process overall
num_filenames = 360
modes = ["c","m","cm","s"]

filename_indices = map(lambda n: n * 4, range(num_filenames))
mode_list = [modes[0]] * 360 + [modes[1]] * 360 + [modes[2]] * 360 + [modes[3]] * 360 


if __name__ == "__main__":
    # number of processes will run simultaneously
    pool = Pool(11)
    results = pool.map(main, zip(filename_indices, mode_list))
