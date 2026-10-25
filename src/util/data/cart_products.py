"""Products list and their prices for the cart page."""

from decimal import Decimal

PRODUCTS: dict[str, Decimal] = {
    "Teddy Bear": Decimal("12.99"),
    "Stuffed Frog": Decimal("10.99"),
    "Handmade Doll": Decimal("10.99"),
    "Fluffy Bunny": Decimal("9.99"),
    "Smiley Bear": Decimal("14.99"),
    "Funny Cow": Decimal("10.99"),
    "Valentine Bear": Decimal("14.99"),
    "Smiley Face": Decimal("9.99"),
}
