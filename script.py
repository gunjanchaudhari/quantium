import csv

def writer(csv_reader, csv_writer):
    for line in csv_reader:
        if(line['product']== 'pink morsel'):
            new_dict = {}
            sales = float(line['price'][1:]) * int(line['quantity'])
            new_dict['Sales'] = sales
            new_dict['Date'] = line['date']
            new_dict['Region'] = line['region']
            csv_writer.writerow(new_dict)


with open('quantium-starter-repo/data/daily_sales_data_0.csv', 'r') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)

    with open('quantium-starter-repo/data/daily_sales_data_1.csv', 'r') as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)

        with open('quantium-starter-repo/data/daily_sales_data_2.csv', 'r') as csv_file3:
            csv_reader3 = csv.DictReader(csv_file3)
    
            with open('quantium-starter-repo/data/daily_sales_data_3.csv','w') as new_file:
                fieldnames = ['Sales', 'Date','Region']
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()
                writer(csv_reader1,csv_writer)
                writer(csv_reader2,csv_writer)
                writer(csv_reader3,csv_writer)
                

    

