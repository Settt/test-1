CREATE SCHEMA test_schema;
CREATE TABLE test_schema.users(
	first_name char(255),
    second_name varchar(255),
    year_born date,
    gender varchar(255)
    );
CREATE TABLE test_schema.new_users_2 AS (SELECT first_name, second_name FROM test_schema.users);
ALTER TABLE test_schema.new_users ADD (salary float);
ALTER TABLE test_schema.new_users MODIFY COLUMN gender ENUM("male", "female", "other");
ALTER TABLE test_schema.new_users DROP COLUMN salary;
ALTER TABLE test_schema.new_users RENAME COLUMN second_name TO last_name;
DROP TABLE test_schema.new_users_2;