# vim: set expandtab ts=4 sw=4 filetype=python fileencoding=utf8:

"""

Catch when we fail to parse a value into a floating point number.

Otherwise, only print successful matches.

"""

import csv

def handle_house_row(row):


    try:
        sale_price = float(row["price"])

    except ValueError as ex:

        print("Sorry, could not parse this data {0!r} into a float!".format(row["price"]))

        # print("Sorry, could not parse this data {price!r} into a float!".format(**row))

        return

    else:
        current_status = row["sourceStatus"]

        allowed_statuses = ["Active", "Back On Market", "Price Reduced"]

        if sale_price < 200 * 1000 and current_status in allowed_statuses:

            print(
                "House at {street} has status {sourceStatus} and price "
                "{price}: good match.".format( **row))

def do_everything():

    home_path_file_name = "home-path.csv"

    home_path_file = open(home_path_file_name, "r")

    csv_thingy = csv.DictReader(home_path_file)

    for house_row in csv_thingy:

        handle_house_row(house_row)



if __name__ == "__main__":

    do_everything()
