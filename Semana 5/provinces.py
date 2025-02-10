import csv

def main():
    prov_list = read_provinces("provinces.txt")
    prov_list.pop(0)
    prov_list.pop()

    print(prov_list)

def read_provinces(filename):
    
    provinces_list = []

    with open(filename, mode="rt") as provinces_file:
        
        reader = csv.reader(provinces_file)
        for row_list in reader:
            province = row_list[0]
            if province == "AB":
                province = "Alberta"
            
            provinces_list.append(province)

    alberta_count = provinces_list.count("Alberta")

    print(f"Count Alberta: {alberta_count}")        
            
    return provinces_list

if __name__ == "__main__":
    main()