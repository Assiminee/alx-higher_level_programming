-- Creates table in database passed as argument
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
