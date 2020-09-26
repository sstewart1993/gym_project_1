DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS members;



CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    age INT,
    gender VARCHAR (255),
    level VARCHAR (255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    time VARCHAR (255),
    date VARCHAR (255),
    duration INT,
    capacity INT
);

CREATE TABLE instructors (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    sessions_id INT REFERENCES sessions(id),
    members_id INT REFERENCES members(id)
);


CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    members_id INT REFERENCES members(id),
    sessions_id INT REFERENCES sessions(id)
);


