
from product import display_product


def test_display_product():
    result = display_product(101, "Laptop", 5, 45000)

    expected = (
        "Product ID : 101\n"
        "Product Name : Laptop\n"
        "Quantity : 5\n"
        "Price : ₹45000.00"
    )

    assert result == expected


def test_another_product():
    result = display_product(102, "Mouse", 10, 500)

    expected = (
        "Product ID : 102\n"
        "Product Name : Mouse\n"
        "Quantity : 10\n"
        "Price : ₹500.00"
    )

    assert result == expected
