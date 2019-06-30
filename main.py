from utils.calculator import Calculator

input_1 = [{
        "quantity": 1,
        "category": ["book"],
        "product_name": "book",
        "price": 12.49
    }, {
        "quantity": 1,
        "category": ["music"],
        "product_name": "music CD",
        "price": 14.99
    }, {
        "quantity": 1,
        "category": ["food"],
        "product_name": "chocolate bar",
        "price": 0.85
}]

input_2 = [{
    "quantity": 1,
    "category": ["imported", "food"],
    "price": 10.00,
    "product_name": "imported box of chocolates"
}, {
    "quantity": 1,
    "category": ["imported"],
    "price": 47.50,
    "product_name": "imported bottle of perfume"
}]

input_3 = [{
    "quantity": 1,
    "category": ["imported", "perfume"],
    "price": 27.99,
    "product_name": "imported bottle of perfume"
}, {
    "quantity": 1,
    "category": ["perfume"],
    "price": 18.99,
    "product_name": "bottle of perfume"
}, {
    "quantity": 1,
    "category": ["medical"],
    "price": 9.75,
    "product_name": "packet of headache pills"
}, {
    "quantity": 1,
    "category": ["food", "imported"],
    "price": 11.25,
    "product_name": "imported box of chocolates"
}]

if __name__ == "__main__":
    print('\n'.join(Calculator().multiple_product(input_1)))
    print('\n')
    print('\n'.join(Calculator().multiple_product(input_2)))
    print('\n')
    print('\n'.join(Calculator().multiple_product(input_3)))
