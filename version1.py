# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""
Read through the file named home-path.csv and print out all houses that
pass all of these tests:

*   Sale price less than $200,000
*   status is any of these:

    *   Active
    *   Back On Market
    *   Price Reduced

Only print the address, sale price, listing agent, and phone number.

"""

import csv

def do_everything():

    home_path_file_name = "home-path.csv"

    home_path_file = open(home_path_file_name, "r")

    csv_thingy = csv.reader(home_path_file)

    header_row = next(csv_thingy)

    print("The header row is {0}.".format(header_row))

    house = next(csv_thingy)

    print("House at {0} has status {1} and price {2}.".format(
        house[0],   # street address
        house[6],   # current status
        house[5]))  # sale price

    sale_price = float(house[5])

    current_status = house[6]

    allowed_statuses = ["Active", "Back On Market", "Price Reduced"]

    if sale_price < 200 * 1000 and current_status in allowed_statuses:
        print("Hurray!  This house is a good match!")

    else:
        print("Sorry, bad match")


if __name__ == "__main__":

    do_everything()
