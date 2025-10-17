def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты, оставляя первые 6 и последние 4 цифры видимыми.
    """
    card = card_number.strip()

    if len(card) != 16 or not card.isdigit():
        raise ValueError("Номер карты должен содержать ровно 16 цифр")

    masked_part_card = "*" * (len(card) - 10)
    result = card[:6] + masked_part_card + card[-4:]
    return result


def mask_account_card(account_number: str) -> str:
    """
    Маскирует номер карты, оставляя последние 4 цифры и "**" перед ними.
    """
    account = account_number.strip()
    masked_account_number = "**" + account[-4:]
    return masked_account_number


def get_date(date_string):
    """
    Возвращает строку с датой.
    """
    date_part = date_string.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"
