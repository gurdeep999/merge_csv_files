import csv
import getfiles

with open('test_merge.csv', 'w', newline="") as merge_file:
    filenames = getfiles.get_files()
    header = []
    rows = []
    for x in filenames:
        with open(x,"r") as file:
            csv_reader = csv.reader(file)
            if filenames.index(x) == 0:
                header = next(csv_reader)
            else:
                next(csv_reader)
            for row in csv_reader:
                rows.append(row)
    csv_writer = csv.writer(merge_file)
    csv_writer.writerow(header)
    csv_writer.writerows(rows)


# file = open('tomerge/1653722853291.csv')
# csv_reader = csv.reader(file)
# header = []
# header = next(csv_reader)
# print(header)
# rows = []
# for row in csv_reader:
#     rows.append(row)
# print(rows)
# file.close()
#
# with open('test.csv','w', newline="") as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow(header)
#     csvwriter.writerows(rows)
#
# print(getfiles.get_files())
