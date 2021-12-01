digits = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
magnitudes = ['', 'Thousand', 'Million', 'Billion']


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = []
        if num < 0:
            sign = 'Negative '
            num = -num
        else:
            sign = ''
        groups = split_num(num)
        for i in range(len(groups)):
            if groups[i] > 0:
                group_res = convert(groups[i])
                if i > 0:
                    group_res.append(magnitudes[i])
                res.append(' '.join(group_res))
        return sign + ' '.join(reversed(res))


def split_num(n):
    groups = []
    while n:
        groups.append(n % 1000)
        n //= 1000
    return groups


def convert(n):
    # 0 < n < 1000
    res = []
    if n >= 100:
        res.append(digits[n // 100])
        res.append('Hundred')
    n = n % 100
    if n >= 20:
        res.append(tens[n // 10])
        if n % 10:
            res.append(digits[n % 10])
    elif n >= 11:
        res.append(teens[n - 10])
    elif n > 0:
        res.append(digits[n])
    return res
