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


number = input("Please enter the account type and number: ")
type, card_number = number.split(maxsplit=1)
print(type, get_mask_number(card_number))
