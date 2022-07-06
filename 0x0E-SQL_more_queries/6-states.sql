-- creates the database hbtn_0d_usa and the tables states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id MEDIUM NOT NULL UNIT AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
	PRIMARY KEY (id)
);
