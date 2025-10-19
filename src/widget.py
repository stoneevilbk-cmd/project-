def get_mask_number(number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры видимыми.
    """
    card = number.strip()

    if len(card) != 16:
        account = number.strip()
        masked_account_number = "**" + account[-4:]
        return masked_account_number
    else:
        masked_part_card = "*" * (len(card) - 10)
        result = card[:6] + masked_part_card + card[-4:]
        return result


number = input("Please enter a number: ")
if number.startswith("4"):
    print("Visa ", get_mask_number(number))

elif number.startswith("5"):
    print("MasterCard ", get_mask_number(number))

elif number.startswith("5"):
    print("MasterCard ", get_mask_number(number))

elif number.startswith("6"):
    print("UnionPay ", get_mask_number(number))

elif number.startswith("22"):
    print("Мир ", get_mask_number(number))

else:
    print("Счет ", get_mask_number(number))