# coding:utf-8
import argparse
import csv
import random

from faker import Faker

fake = Faker()


def gen_password():
    password = ""
    strings = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    pass_len = random.randint(8, 16)
    for i in range(pass_len):
        password += strings[random.randrange(len(strings))]
    return password


def gen_user():
    email = fake.email()
    username = email[:email.index("@")]
    domain = email[email.index("@"):]
    return username, email, domain


def main():
    parser = argparse.ArgumentParser(description='generate fake user account for password list attack')
    parser.add_argument('-l', '--length',  type=int, required=True, help='number of fake user account')
    parser.add_argument('-t', '--usertype',  type=str, choices=['random', 'increment'], required=True, help='type of username random or increment such as user01, user02...')
    parser.add_argument('-o', '--output',  type=str, default="account_list.csv", help='output csv file of fake accounts')
    args = parser.parse_args()

    array = []

    if args.usertype == "random":
        for i in range(args.length):
            user = gen_user()
            array.append([user[0], user[1], gen_password()])

    elif args.usertype == "increment":
        user = gen_user()
        username = gen_user()[0]
        domain = gen_user()[2]
        for i in range(args.length):
            array.append([username + str(i), username + str(i) + domain, gen_password()])

    with open(args.output, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(array)


if __name__ == "__main__":
    main()
