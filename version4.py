# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Now, write out a new file that has the matches in CSV format.

And round the prices to the nearest thousand.

Also, show the count of how many houses match.

"""

import csv

def handle_house_row(out_csv_thingy, row):

    # Just skip bad rows.
    try:
        sale_price = float(row["price"])

    except ValueError as ex:
        return

    else:
        current_status = row["sourceStatus"]

        allowed_statuses = ["Active", "Back On Market", "Price Reduced"]

        if sale_price < 200 * 1000 and current_status in allowed_statuses:

            rounded_price = round(sale_price, -3)

            # print("Original price: {0}, sales price: {1}".format( sale_price, rounded_price))

            out_row = dict({
                "street address" :row["street"],
                "rounded price": rounded_price,
                "status": current_status})

            out_csv_thingy.writerow(out_row)


def do_everything():

    home_path_file_name = "home-path.csv"

    home_path_file = open(home_path_file_name, "r")

    csv_thingy = csv.DictReader(home_path_file)

    out_csv_file = open("matching-houses.csv", "w")

    out_csv_thingy = csv.DictWriter(
        out_csv_file,
        ["street address", "status", "rounded price"])

    for house_row in csv_thingy:

        handle_house_row(out_csv_thingy, house_row)

    out_csv_file.close()

    print("Matching houses are in matching-houses.csv")


if __name__ == "__main__":

    do_everything()
