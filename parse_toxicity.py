import csv

file_output = open('toxic_sentences.csv', mode='w')
writer = csv.writer(file_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


with open('toxicity_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    num_toxic = 0
    for row in csv_reader:
        is_toxic = False
        if row[2] == '1' or row[3] == '1' or row[4] == '1' or row[5] == '1' or row[6] == '1':
            num_toxic += 1
            is_toxic = True

        if is_toxic:
            writer.writerow([row[1], "1"])
        else:
            writer.writerow([row[1], "0"])

    print("The number of toxic entries: " + str(num_toxic))
