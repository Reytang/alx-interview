#!/usr/bin/python3
""" UTF-8 Validations """


def validUTF8(data):
    """
    the Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    number_bytes = 0

    mask_2 = 1 << 7
    mask_4 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & mask_2 and not (i & mask_4)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
