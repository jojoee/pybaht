from typing import List
import re
import math

# constants
DEFAULT_RESULT = 'ศูนย์บาทถ้วน'
SINGLE_UNIT_STRS = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
PLACE_NAME_STRS = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']
SATANG_FORMAT = "{:.2f}"


def num2word(nums: List[int]) -> str:
    global SINGLE_UNIT_STRS

    result: List[str] = []
    num_len: int = len(nums)
    max_len: int = 7

    if num_len > max_len:
        # more than a million
        overflow_index = num_len - max_len + 1
        return num2word(nums[0:overflow_index]) + 'ล้าน' + num2word(nums[overflow_index:])
    else:
        for i, digit in enumerate(nums):
            if digit > 0:
                result.append(SINGLE_UNIT_STRS[digit] + PLACE_NAME_STRS[num_len - i - 1])

    return ''.join(result)


def grammar_fix(s: str) -> str:
    result = s
    result = result.replace('หนึ่งสิบ', 'สิบ')
    result = result.replace("สองสิบ", 'ยี่สิบ')
    result = result.replace("สิบหนึ่ง", 'สิบเอ็ด')

    return result


def combine(baht: str, satang: str) -> str:
    """
    Combine baht and satang and also adding unit
    """
    global DEFAULT_RESULT

    parts: List[str] = []

    if baht:
        parts.append(baht)
        parts.append("บาท")

    if satang:
        parts.append(satang)
        parts.append("สตางค์")

    if not parts:
        return DEFAULT_RESULT
    elif not satang:
        parts.append("ถ้วน")

    return "".join(parts)


def bahttext(num: float = 0) -> str:
    """
    Change number to Thai pronunciation string
    """
    global SATANG_FORMAT

    # only int and float
    if type(num) not in (float, int):
        return DEFAULT_RESULT

    # set
    positive_num = abs(num)

    # check if it's zero upfront to avoid unnecessary calculations
    if positive_num == 0:
        return DEFAULT_RESULT

    # split baht and satang e.g. 432.214567 >> 432, 21
    baht_str: str = str(math.floor(positive_num))
    satang_str = SATANG_FORMAT.format(positive_num % 1 * 100).split('.')[0]
    baht_arr: List[int] = [int(s) for s in baht_str]
    satang_arr: List[int] = [int(s) for s in satang_str]

    # proceed
    baht = num2word(baht_arr)
    satang = num2word(satang_arr)

    # grammar
    baht = grammar_fix(baht)
    satang = grammar_fix(satang)

    # combine
    result = combine(baht, satang)

    return result if num >= 0 else 'ลบ' + result
