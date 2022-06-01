from typing import List
import re
import math

# constants
DEFAULT_RESULT = 'ศูนย์บาทถ้วน'
SINGLE_UNIT_STRS = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
PLACE_NAME_STRS = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']


def num2word(nums: List[int]) -> str:
    global SINGLE_UNIT_STRS

    result: str = ''
    num_len: int = len(nums)
    max_len: int = 7

    if num_len > max_len:
        # more than million
        overflow_index: int = num_len - max_len + 1
        overflow_nums: List[int] = nums[0:overflow_index]
        remaining_numbs: List[int] = nums[overflow_index:]
        return num2word(overflow_nums) + 'ล้าน' + num2word(remaining_numbs)
    else:
        for i in range(len(nums)):
            digit = nums[i]
            if digit > 0:
                result += SINGLE_UNIT_STRS[digit] + PLACE_NAME_STRS[num_len - i - 1]

    return result


def grammar_fix(s: str) -> str:
    """
    @todo improve performance
    """
    result = s
    result = re.sub('หนึ่งสิบ', 'สิบ', result)
    result = re.sub("สองสิบ", 'ยี่สิบ', result)
    result = re.sub("สิบหนึ่ง", 'สิบเอ็ด', result)

    return result


def combine(baht: str, satang: str) -> str:
    """
    Combine baht and satang and also adding unit
    """
    global DEFAULT_RESULT

    if baht == '' and satang == '':
        return DEFAULT_RESULT
    elif baht != '' and satang == '':
        return baht + 'บาท' + 'ถ้วน'
    elif baht == '' and satang != '':
        return satang + 'สตางค์'
    else:
        return baht + 'บาท' + satang + 'สตางค์'


def bahttext(num: float = 0) -> str:
    """
    Change number to Thai pronunciation string
    """
    # only int and float
    if type(num) not in (float, int):
        return DEFAULT_RESULT

    # set
    positive_num = abs(num)

    # split baht and satang e.g. 432.214567 >> 432, 21
    baht_str: str = str(math.floor(positive_num))
    satang_str = "{:.2f}".format(positive_num % 1 * 100).split('.')[0]
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
