# Work_req1_PRO2002

In this assignment, I refactored three small Python examples.

## 1. Vehicle Inheritance

### The problem

In the original code, `Bicycle` inherited the `start_engine()` method from `Vehicle`. Because a bicycle does not have an engine, the method had to raise an exception. I thought this was a design problem because `Bicycle` received behavior that it could not use.

### What I changed

I added a general `Vehicle` class with a `move()` method. I then created `EngineVehicle`, which inherits from `Vehicle` and adds `start_engine()`. The `Bicycle` class inherits directly from `Vehicle`, so it only receives the `move()` behavior.

This follows the **Liskov Substitution Principle** because `Bicycle` can now be used as a `Vehicle` without causing an exception because of an unsupported method.

## 2. Order Creation

### The problem

The original `OrderProcessor` used an `if/elif` statement to choose between `OnlineOrder`, `StoreOrder`, and `PhoneOrder`. This worked, but the method would become longer if more order types were added.

### What I changed

I created an `OrderFactory` with an `order_types` dictionary. The dictionary connects each order-type string to the correct class. The `create_order()` method looks up the requested class and creates an object from it.

If the order type does not exist, the method raises a `ValueError` that shows the unknown value. I used the **Factory pattern** because the class is responsible for creating order objects. This also supports the **Open/Closed Principle**, since I can add another order type to the dictionary without changing the `create_order()` method.

## 3. User Management

### The problem

The original `UserManager` class had several responsibilities. It stored user information, saved users to a database, sent welcome emails, and generated reports. I thought this made the class harder to understand and maintain.

### What I changed

I separated these responsibilities into four classes:

- `User` stores the username and email.
- `UserRepository` saves a user to the database.
- `EmailService` sends the welcome email.
- `UserReport` generates the user report.

This follows the **Single Responsibility Principle** because each class now has one clear task. For example, changing how emails are sent would only require changes to `EmailService`.

## Reflection

While working on these examples, I learned that refactoring does not always require a complicated solution. In the vehicle example, I changed the inheritance structure so that `Bicycle` only receives behavior that makes sense for it. In the order example, I replaced the repeated conditions with a Factory and a dictionary. In the user example, I separated one large class into smaller classes with clear responsibilities. These changes made the code easier for me to understand and should also make it easier to test and extend later. The exercise helped me understand how SOLID principles can be applied to simple, practical Python code.
