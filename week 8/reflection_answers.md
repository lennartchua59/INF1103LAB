# INF1103 Lab 6 (Week 8) - Reflection Answers

1. **Class vs object?** A class is the blueprint (attributes and methods). An object is one actual thing built from it. `Product` is the class; `Product("P001", "Laptop", 1200.00, 15)` is an object.

2. **Why is Product a suitable class?** The store is full of products. Each has the same kind of data and the same behaviour, so one blueprint can create many objects.

3. **What data belongs inside a Product?** Product ID, name, price and stock quantity.

4. **Why should Product manage its own stock?** So the class controls how the value changes. `update_stock()` rejects negative numbers, so the main program can't put the product into an invalid state. The rule lives in one place.

5. **What does encapsulation mean in my program?** The data is private (`__product_id`, `__name`, `__price`, `__stock`) and is only read through getters or changed through `update_stock()`. Likewise, `Inventory` keeps its list private (`__products`) and offers methods to work with it.

6. **Responsibility of Product?** Represent and manage one product: store its information, manage its own stock, and display its own information.

7. **Responsibility of Inventory?** Manage a collection of products: store them, add them, search them and display them.

8. **How does this show SRP?** Each class has one reason to change. Product changes only if what a product is changes, and Inventory only if how the collection is managed changes. Neither handles menus, user input or files; those stay in the main program.

9. **What does the main program need to know about a Product?** Only its public interface: how to create one, the getters (`get_product_id()`, `get_name()`, `get_price()`, `get_stock()`), and the methods `update_stock()` and `display_information()`.

10. **What doesn't the main program need to know?** How Product stores its data (the private `__` attributes, name mangling), or how `update_stock()` validates a value. The internals could change without breaking the main program.
