import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """Lee un archivo CSV y lo almacena en un diccionario con la clave especificada."""
    file_dict = {}
    try:
        with open(filename, mode="rt") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=",")
            next(csv_reader)  # Saltar encabezado
            for row in csv_reader:
                key = row[key_column_index]
                file_dict[key] = row
        return file_dict
    except FileNotFoundError as fnf_error:
        print("Error: missing file")
        print(fnf_error)
        return None  # Retorna None para indicar que el archivo no se encontró


def main():
    KEY_INDEX = 0
    PRODUCT_CODE_INDEX = 0
    PRODUCT_NAME = 1
    PRODUCT_PRICE = 1
    PRODUCT_COST = 2

    # Intentar leer el archivo de productos
    product_dict = read_dictionary("products.csv", KEY_INDEX)

    # Si no se encontró el archivo, salir del programa
    if product_dict is None:
        return  

    print("Inkom Emporium")
    now = datetime.now()

    total_items = 0
    subtotal = 0

    try:
        with open("request.csv", mode="rt") as csvreceipt:
            csv_reader_request = csv.reader(csvreceipt, delimiter=",")
            next(csv_reader_request)  # Saltar encabezado

            for row in csv_reader_request:
                product_code = row[PRODUCT_CODE_INDEX]
                product_quantity = int(row[PRODUCT_PRICE])

                try:
                    # Intentar obtener el producto del diccionario
                    product_name = product_dict[product_code][PRODUCT_NAME]
                    product_cost = float(product_dict[product_code][PRODUCT_COST])

                    subtotal += product_quantity * product_cost
                    total_items += product_quantity
                    print(f"{product_name} {product_quantity} @ {product_cost}")

                except KeyError:
                    # Lanzar una excepción en lugar de solo imprimir un mensaje
                    raise KeyError(f"Error: unknown product ID in the request.csv file\n'{product_code}'")

        # Calcular impuestos y total
        tax_subtotal = subtotal * 0.06
        total = subtotal + tax_subtotal

        # Imprimir resumen
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {round(subtotal, 2)}")
        print(f"Sales Tax: {round(tax_subtotal, 2)}")
        print(f"Total: {round(total, 2)}")
        print("Thank you for shopping at the Inkom Emporium.")

        formatted_time = now.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_time)

    except FileNotFoundError as fnf_error:
        print("Error: missing file")
        print(fnf_error)

    except KeyError as key_error:
        print(key_error)  # Imprime el mensaje del KeyError y detiene el programa


if __name__ == "__main__":
    main()