-- Inserting data into product table
INSERT INTO product (product_id, name)
VALUES
  (1, 'Product A'),
  (2, 'Product B'),
  (3, 'Product C');

-- Inserting data into country table
INSERT INTO country (country_id, country_name)
VALUES
  (1, 'Country A'),
  (2, 'Country B'),
  (3, 'Country C');

-- Inserting data into city table
INSERT INTO city (city_id, city_name, country_id)
VALUES
  (1, 'City A', 1),
  (2, 'City B', 2),
  (3, 'City C', 3);

-- Inserting data into store table
INSERT INTO store (store_id, name, city_id)
VALUES
  (1, 'Store A', 1),
  (2, 'Store B', 2),
  (3, 'Store C', 3);

-- Inserting data into users table
INSERT INTO users (user_id, name)
VALUES
  (1, 'User A'),
  (2, 'User B'),
  (3, 'User C');

-- Inserting data into status_name table
INSERT INTO status_name (status_name_id, status_name)
VALUES
  (1, 'Status 1'),
  (2, 'Status 2'),
  (3, 'Status 3');

-- Inserting data into sale table
INSERT INTO sale (sale_id, amount, date_sale, product_id, user_id, store_id)
VALUES
  ('Sale1', 10.50, CURRENT_TIMESTAMP, 1, 1, 1),
  ('Sale2', 15.25, CURRENT_TIMESTAMP, 2, 2, 2),
  ('Sale3', 20.75, CURRENT_TIMESTAMP, 3, 3, 3);

-- Inserting data into order_status table
INSERT INTO order_status (order_status_id, update_at, sale_id, status_name_id)
VALUES
  ('OrderStatus1', CURRENT_TIMESTAMP, 'Sale1', 1),
  ('OrderStatus2', CURRENT_TIMESTAMP, 'Sale2', 2),
  ('OrderStatus3', CURRENT_TIMESTAMP, 'Sale3', 3);
