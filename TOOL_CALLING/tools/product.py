def search_product(
    product_name: str
) -> list:
    """
    Search for products by name.
    """

    products = [

        {
            "name": "MacBook Air M4",
            "price": 99999,
            "category": "Laptop"
        },

        {
            "name": "iPhone 17",
            "price": 79999,
            "category": "Phone"
        },

        {
            "name": "Samsung Galaxy S26",
            "price": 74999,
            "category": "Phone"
        },

        {
            "name": "Dell XPS 15",
            "price": 125000,
            "category": "Laptop"
        }
    ]

    results = []

    for product in products:

        if product_name.lower() in product["name"].lower():

            results.append(product)

    return results