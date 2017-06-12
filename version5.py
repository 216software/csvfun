# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:
# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
A baby step toward writing tests, and I count up the number of
matches.
"""

import csv

def handle_house_row(out_csv_thingy, row):

    """
    If the house is good enough, then this will write it in the
    spreadsheet.

    Also, this will return None when the house fails, and will return
    a dictionary when the house is good.

    Example:
    >>> row = {"price": 1000 * 1000, "sourceStatus": "Active", "street": "123 Elm Street"}
    >>> handle_house_row(None, row) is None
    True


    """

    try:
        sale_price = float(row["price"])

    except ValueError as ex:
        return

    else:
        current_status = row["sourceStatus"]

        allowed_statuses = ["Active", "Back On Market", "Price Reduced"]

        if sale_price < 200 * 1000 and current_status in allowed_statuses:

            rounded_price = round(sale_price, -3)

            out_row = dict({
                "street address" :row["street"],
                "rounded price": rounded_price,
                "status": current_status})

            out_csv_thingy.writerow(out_row)

            return out_row

def do_everything():

    home_path_file_name = "home-path.csv"

    home_path_file = open(home_path_file_name, "r")

    csv_thingy = csv.DictReader(home_path_file)

    out_csv_file = open("matching-houses.csv", "w")

    out_csv_thingy = csv.DictWriter(
        out_csv_file,
        ["street address", "status", "rounded price"])

    matching_houses = 0

    for row_number, house_row in enumerate(csv_thingy, start=1):

        matching_house = handle_house_row(out_csv_thingy, house_row)

        if matching_house:
            matching_houses += 1


    out_csv_file.close()

    print(
        "There are {0} matching houses in matching-houses.csv, "
        "out of {1} checked.".format(matching_houses, row_number))

if __name__ == "__main__":

    do_everything()
