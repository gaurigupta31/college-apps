-- create table to store information about the users who sign up
-- notion_id and page_id are cleared from the database if notion access is removed

CREATE TABLE IF NOT EXISTS USER_INFO(
        id BIGSERIAL NOT NULL PRIMARY KEY, 
        email VARCHAR(150) NOT NULL,
        salt VARCHAR(300),
        vkey VARCHAR(300),
        notion_id VARCHAR(150),
        page_id VARCHAR(150); 