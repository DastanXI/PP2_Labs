import re

def parse_receipt(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    items = []
    i = 0
    while i < len(lines):
        if re.match(r'\d+\.', lines[i]):
            item = {}
            item['name'] = lines[i + 1]

            qty_price_match = re.match(r'(\d[\d\s]*,[\d]+)\s*x\s*(\d[\d\s]*,[\d]+)', lines[i + 2])
            if qty_price_match:
                q = qty_price_match.group(1).replace(' ', '').replace(',', '.')
                p = qty_price_match.group(2).replace(' ', '').replace(',', '.')
                item['quantity'] = float(q)
                item['unit_price'] = float(p)

            total_line = lines[i + 3].replace(' ', '').replace(',', '.')
            item['total'] = float(total_line)

            items.append(item)
            i += 6
        else:
            i += 1

    result = {'items': items}
    for idx, line in enumerate(lines):
        if 'ИТОГО' in line.upper():
            result['total'] = float(lines[idx + 1].replace(' ', '').replace(',', '.'))
        if re.search(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}', line):
            result['datetime'] = line
        if 'г. Нур' in line:
            result['address'] = line

    return result

# Example usage
if __name__ == '__main__':
    data = parse_receipt('row.txt')
    for i, item in enumerate(data['items'], 1):
        print(f"{i}. {item['name']}: {item['quantity']} x {item['unit_price']} = {item['total']}")

    print("\nИТОГО:", data.get('total'))
    print("Дата и время:", data.get('datetime'))
    print("Адрес:", data.get('address'))
