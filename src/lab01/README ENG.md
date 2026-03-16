# LR-1 — Class and Package (Python 3.x)

# Project Objective (Variant 3)

* Master custom class declaration
* Understanding encapsulation (private fields)
* Implementing properties (@property)
* Overriding magic methods (`__str__`, `__repr__`, `__eq__`)
* Understanding the difference between class and instance attributes

# About the Project
## Product Class
This project implements a custom **Product** class that models a product in an online sales system. The class contains its own attribute: "store_name", which defines the name of the store to which the products belong; and also contains the attributes of the objects: product name, price, stock, and product model. The logical state of the product (active or inactive) has also been implemented.

### Class Attribute:
* store_name: attribute to name the store.

### Instance Attributes (Private Fields):
* _name - product name
* _price - product price
* _estoque - quantity in store stock
* _model - product model
* _is_active - product status (active / deactivated)
### Properties (@property):
* Read: name - product name
* Read and Write: price - product price
* Read: estoque - quantity in store stock
* Read: model - product model
* Read: is_active - product status (active/deactivated)
### Magic Methods:
* `__str__` — Convenient presentation of product information, readable for the user
* `__repr__` — technical representation of a product - only for developers
* `__eq__` — comparison of products by name and model
### Business Methods:
* deactivate() - deactivates a product
* eactivate() - activates a product
* apply_discount(percentage) - applies a discount to the product
* sell(self, quantity) - sells the product

*[See complete validation.py code](../libraries/validation.py)* | *[See complete model.py code](model.py)* | *[See complete demo.py code](demo.py)*
# Project Demonstration
**1. Stress Tests (Validation and Robustness)**
* **try/except blocks:** Instead of the program "crashing," it will return specific errors (empty name, short model, negative price, negative stock) to prove that the *[validation.py](../libraries/validation.py)* file is protecting the Product class.

![test validation](../../images/lab01/teste_validação.png)

**2 . Inventory Audit (The Heart of the Logic)**
**Inventory with nested for loop:** By iterating through the inventory list comparing each item with the following ones, the program generates a real quality control scenario, verifying which products are the same in name and model.

**Interaction with `__eq__`:** The command "if inventory[i] == inventory[j]" causes Python to automatically execute the code written in *[model.py](model.py)*, triggering the Warning and the suggestion to unify stock. This automates store management.

![product comparison](../../images/lab01/comparação%20de%20produtos.png)

**3. Visualization Perspectives**
**User vs. Programmer:** For a stylish and user-friendly visualization, we use `__str__` (readable and with currency), and for the developer, we use `__repr__` (technical). This greatly helps in debugging large systems.

![Product Listing](../../images/lab01/Listagem%20de%20produtos.png)
**4. Lifecycle and Business Rules**
* **Flow Test:** A real sequence was simulated: disable -> attempt to sell (block) -> enable -> successful sale.

* **Data Limit:** attempt to sell a quantity of product greater than what is in stock: The system proves that it respects the physical quantity available, not allowing "phantom" sales.

![Business Execution](../../images/lab01/Realização%20de%20Negócios.png)

**5. Handling Class and Instance Attributes**
**Class Attributes:** Changing the class attribute of the class itself affects all instances. This is considered a "Global Change".
**Instance Attributes:** Changing the class attribute from a class instance (object) affects only that object, without affecting other objects. This is considered a "Local Change". In the project, the store name was tested using the class and instance attribute through the general plan, that is, via the class (Product.store_name) or a specific object (p3.store_name).

**Final Stock Status:** The project is consistent and can update the store's stock and the current product statuses.

![Handling local and global attributes](../../images/lab01/Manipulação.png)