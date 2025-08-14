from collections import OrderedDict


if __name__ == '__main__':
    # Read the number of items
    n = int(input())
    ordered_dict = OrderedDict()
    for _ in range(n):
        item = input().split()
        item_name = ' '.join(item[:-1])
        item_price = int(item[-1])
        if item_name not in ordered_dict:
            ordered_dict[item_name] = item_price
        else:
            ordered_dict[item_name] += item_price

    for item_name, item_price in ordered_dict.items():
        print(f"{item_name} {item_price}")
