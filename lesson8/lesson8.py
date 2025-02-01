import logging

print("======== Logging ========")
logging.basicConfig(level=logging.DEBUG,
                    filename="mylogs.log",
                    filemode="w",
                    format="My logs message:%(asctime)s:%(levelname)s:%(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

try:
    print(10 / 0)
except Exception as e:
    logging.exception("Exception")

print("======== Testing ========")

if 2 + 2 == 4:
    print("2 + 2 = 4")

assert 2 + 2 == 4, "wrong assert"

print("======== Доктести ========")

print("======== Unit tests ========")


def adder(*args, **kwargs):
    result = 0
    for i in args:
        result += i

    for i in kwargs.values():
        result += i
    return result


def sum(num1, num2):
    return num1 + num2
