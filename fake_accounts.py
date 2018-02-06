# coding:utf-8
import random

from faker import Faker


def create_password():
    strings = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    pass_len = random.randint(8, 16)
    mypw = ""

    for i in range(pass_len):
        mypw += strings[random.randrange(len(strings))]

    print(mypw)


def main():
    # fake = Faker()
    # for i in range(3):
    #     print(fake.email())
    create_password()


if __name__ == "__main__":
    main()
