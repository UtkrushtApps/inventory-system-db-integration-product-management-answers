# Solution Steps

1. Define a normalized PostgreSQL table for products with columns: id (PK), name (unique, indexed, not null), description (nullable), price (numeric, not null), quantity (not null, default 0), created_at (timestamp, not null, defaults to now).

2. In the SQLAlchemy models (models.py), define a Product class with these columns and proper SQLAlchemy types, including unique and index constraints.

3. Create Pydantic schemas (schemas.py) for product creation (input) and reading (output), including strict validation for price and quantity.

4. Implement an async data access layer (crud.py) with two functions: add_product (for inserting a new product, handling SQL errors like IntegrityError) and get_all_products (for listing all products). Use SQLAlchemy's async session and query API.

5. Configure the async database connection (db.py) using SQLAlchemy's async engine and a sessionmaker that yields AsyncSession objects for FastAPI dependencies.

6. Write a migration script (alembic/versions/...) that creates the products table with the defined schema, including all constraints and indexing.

7. Plug these implementations into the FastAPI app's routing and dependency system (not needed in this task—the provided code expects a data layer in this form).

