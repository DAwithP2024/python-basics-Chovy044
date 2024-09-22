# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# 展示商品类别
def display_categories():
    for index, category in enumerate(products.keys(), 1):
        print(f"{index}. {category}")
    return None

# 展示某个类别的商品
def display_products(products_list):
    for index, product in enumerate(products_list, 1):
        print(f"{index}. {product[0]} - ${product[1]}")

# 根据价格对商品进行排序
def display_sorted_products(products_list, sort_order):
    if sort_order.lower() == 'asc' or sort_order == '1':  # 升序
        sorted_products = sorted(products_list, key=lambda x: x[1])
    elif sort_order.lower() == 'desc' or sort_order == '2':  # 降序
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("Invalid order")
        return []
    for index, product in enumerate(sorted_products, 1):
        print(f"{index}. {product[0]} - ${product[1]}")
    return sorted_products

# 验证姓名
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

# 验证邮箱
def validate_email(email):
    return "@" in email

# 添加商品到购物车
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# 展示购物车内容
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your cart contains:")
        for product, price, quantity in cart:
            print(f"{product} - ${price} x {quantity} = ${price * quantity}")
        total_cost = sum(price * quantity for _, price, quantity in cart)
        print(f"Total cost: ${total_cost}")
    return total_cost

# 生成收据
def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products purchased:")
    for product, price, quantity in cart:
        print(f"{product} - ${price} x {quantity} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

# 主程序
def main():
    cart = []

    # 获取用户姓名并验证
    name = input("Enter your name (first and last): ")
    while not validate_name(name):
        print("Invalid name. Please enter both first and last names, and ensure they only contain alphabets.")
        name = input("Enter your name (first and last): ")

    # 获取用户邮箱并验证
    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email with an '@' symbol.")
        email = input("Enter your email: ")

    # 开始购物流程
    while True:
        print("\nCategories available for shopping:")
        display_categories()
        
        # 选择类别
        try:
            category_choice = int(input("\nSelect a category (number): "))
            if category_choice not in range(1, len(products) + 1):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid category number.")
            continue

        selected_category = list(products.keys())[category_choice - 1]
        print(f"\nProducts in {selected_category}:")
        selected_products = products[selected_category]
        display_products(selected_products)

        # 选择商品或排序
        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            
            try:
                option = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if option == 1:
                try:
                    product_choice = int(input("Enter the product number: "))
                    if product_choice not in range(1, len(selected_products) + 1):
                        raise ValueError
                    product = selected_products[product_choice - 1]
                    quantity = int(input(f"Enter quantity for {product[0]}: "))
                    add_to_cart(cart, product, quantity)
                    print(f"{quantity} {product[0]}(s) added to cart.")
                except ValueError:
                    print("Invalid input. Please try again.")
                    
            elif option == 2:
                sort_order = input("Sort by price: 'asc' for ascending, 'desc' for descending, '1' for ascending, '2' for descending: ")
                sorted_products = display_sorted_products(selected_products, sort_order)
                selected_products = sorted_products

            elif option == 3:
                break

            elif option == 4:
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Enter delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something next time. Have a nice day!")
                return

            else:
                print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()