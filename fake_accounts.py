# coding:utf-8
import argparse
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
    return username, email


def main():
    parser = argparse.ArgumentParser(description='generate fake user account for password list attack')
    parser.add_argument('-l', '--length',  type=int, required=True, help='number of fake user account')
    parser.add_argument('-t', '--usertype',  type=str, choices=['random', 'increment'], required=True, help='type of username random or increment such as user01, user02...')
    parser.add_argument('-o', '--output',  type=str, default="account_list.csv", help='output csv file of fake accounts')
    args = parser.parse_args()
    # print(args)
    for i in range(args.length):
        print(gen_user())
        print(gen_password())


if __name__ == "__main__":
    main()
