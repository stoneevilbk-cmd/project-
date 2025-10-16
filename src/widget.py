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


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер карты, оставляя последние 4 цифры и "**" перед ними.
    """
    account = account_number.strip()
    masked_account_number = "**" + account[-4:]
    return masked_account_number