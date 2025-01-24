import frappe

@frappe.whitelist()
def money_in_chinese(number):
    chinese_nums = {
        '0': '零',
        '1': '壹',
        '2': '贰',
        '3': '叁',
        '4': '肆',
        '5': '伍',
        '6': '陆',
        '7': '柒',
        '8': '捌',
        '9': '玖'
    }
    
    units = ['', '拾', '佰', '仟', '万']
    
    # Convert number to string with 2 decimal places
    num_str = "{:.2f}".format(float(number))
    integer_part, decimal_part = num_str.split('.')
    
    result = ''
    
    # Process integer part
    for i, digit in enumerate(integer_part):
        if digit != '0':
            result += chinese_nums[digit] + units[len(integer_part) - i - 1]
    
    result += '圆'
    
    # Process decimal part
    if decimal_part != '00':
        jiao = decimal_part[0]
        fen = decimal_part[1]
        
        if jiao != '0':
            result += chinese_nums[jiao] + '角'
        if fen != '0':
            result += chinese_nums[fen] + '分'
    else:
        result += '整'
    
    return result
