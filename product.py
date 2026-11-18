
def display_product(product_id, name, quantity, price):
    """
    Accept product details and return formatted product information.
    """
    return (
        f"Product ID : {product_id}\n"
        f"Product Name : {name}\n"
        f"Quantity : {quantity}\n"
        f"Price : ₹{price:.2f}"
    )


# Example usage
if __name__ == "__main__":
    result = display_product(101, "Laptop", 5, 45000)
    print(result)
