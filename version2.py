# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Use a csv.DictReader instead of a csv.reader.  Actually loop through all
the rows instead of just dying after the first.
"""

import csv

def handle_house_row(row):

    print(
        "House at {street} has status {sourceStatus} and price {price}.".format(
            **row))

    sale_price = float(row["price"])

    current_status = row["sourceStatus"]

    allowed_statuses = ["Active", "Back On Market", "Price Reduced"]

    if sale_price < 200 * 1000 and current_status in allowed_statuses:
        print("Hurray!  This house is a good match!")

    else:
        print("Sorry, bad match")


def do_everything():

    home_path_file_name = "home-path.csv"

    home_path_file = open(home_path_file_name, "r")

    csv_thingy = csv.DictReader(home_path_file)

    for house_row in csv_thingy:

        handle_house_row(house_row)



if __name__ == "__main__":

    do_everything()
