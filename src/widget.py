from src.masks import get_mask_account, get_mask_card_number


def get_mask_number(number: str) -> str:
    """
    Маскирует номер карты или счета, оставляя первые 6 и последние 4 цифры видимыми.
    """
    number = number.strip()
    type, number = number.rsplit(maxsplit=1)
    if len(number) != 16:
        return type + " " + get_mask_account(number)
    else:
        return f"{type} {get_mask_card_number(number)}"

def get_date(date: str) -> str:
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

number = input("Please enter the account type and number: ")
print(get_mask_number(number))

print(get_date("2024-03-11T02:26:18.671407"))
# test_1 = "Visa Platinum 7000792289606361"
# test_2 = "Счет 73654108430135874305"
# print(get_mask_number(test_1), get_mask_number(test_2))