#Base convertion

def base_conv(num, base):
    base_str = "0123456789ABCDEF"
    if num < base:
        return base_str[num]
    else:
        return  base_conv(num//base, base) + base_str[num%base]

print(base_conv(31, 16))
