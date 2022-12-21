from cart.cart import Cart


def generate_price(cart: Cart) -> float:
    price = 0.00
    for i in range(len(cart.prices)):
        price += cart.prices[i] * cart.quantitites[i]
    return price


def generate_half_first(cart: Cart) -> float:
    price = cart.prices[0] * cart.quantitites[0] * 0.5
    for i in range(1, len(cart.prices)):
        price += cart.prices[i] * cart.quantitites[i]
    return price


def generate_half_last(cart: Cart) -> float:
    price = cart.prices[len(cart.prices)-1] * cart.quantitites[len(cart.prices)-1] * 0.5
    for i in range(len(cart.prices)-1):
        price += cart.prices[i] * cart.quantitites[i]
    return price


def generate_invoice(cart: Cart) -> str:
    price = 0.00
    currency = ""
    match cart.reduction:
        case "STANDARD":
            price = generate_price(cart)
        case "HALF":
            price = generate_price(cart) * 0.5
        case "TENTH":
            price = generate_price(cart) * 0.1
        case "HALF_FIRST":
            price = generate_half_first(cart)
        case "HALF_LAST":
            price = generate_half_last(cart)
    match cart.country:
        case "FR":
            currency = "€"
        case "UK":
            currency = "£"
            price *= 1.42
        case "US":
            currency = "$"
            price *= 1.314
    return f'{price:.2f}' + " " + currency
