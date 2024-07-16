import requests

def get_categories():
    response = requests.get("https://fakestoreapi.com/products/categories")
    return response.json()

def get_products_by_category(category):
    response = requests.get(f"https://fakestoreapi.com/products/category/{category}")
    return response.json()

def main():
    categories = get_categories()
    print("Категории товаров:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    choice = int(input("Введите номер категории, чтобы посмотреть товары: ")) - 1
    if 0 <= choice < len(categories):
        selected_category = categories[choice]
        products = get_products_by_category(selected_category)
        print(f"\nТовары в категории '{selected_category}':")
        for product in products:
            print(f"Название: {product['title']}")
            print(f"Цена: ${product['price']}")
            print(f"Описание: {product['description']}")
            print("-" * 40)
    else:
        print("Неверный выбор категории.")

if __name__ == "__main__":
    main()