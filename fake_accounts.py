# coding:utf-8
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
    print(gen_user())
    print(gen_password())


if __name__ == "__main__":
    main()
