-- Create tables for data to be loaded into
DROP TABLE beers;
DROP TABLE styles;
DROP TABLE breweries;
DROP TABLE beer_reviews;
DROP TABLE categories;

CREATE TABLE beer_reviews (
    id INTEGER PRIMARY KEY NOT NULL,
    review_overall DECIMAL(7,6) NOT NULL
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY NOT NULL,
    cat_name VARCHAR(30)   NOT NULL
);

CREATE TABLE styles (
    id INTEGER PRIMARY KEY NOT NULL,
    cat_id INTEGER   NOT NULL,
    style_name VARCHAR(75)   NOT NULL,
    abv_low DECIMAL(3,1)   NOT NULL,
    abv_high DECIMAL(3,1)   NOT NULL,
    glass_type VARCHAR(20)   NOT NULL,
    FOREIGN KEY (cat_id) REFERENCES categories (id)
);

CREATE TABLE breweries (
    id INTEGER PRIMARY KEY NOT NULL,
    brewery_name VARCHAR(100)   NOT NULL,
    address1 VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    phone VARCHAR(20),
    website VARCHAR(100),
    FOREIGN KEY (id) REFERENCES beer_reviews (id)
);

CREATE TABLE beers (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(100)   NOT NULL,
    brewery_id INTEGER   NOT NULL,
    cat_id INTEGER   NOT NULL,
    style_id INTEGER   NOT NULL,
    abv VARCHAR(15)   NOT NULL,
    FOREIGN KEY (brewery_id) REFERENCES breweries (id)
);

-- Joins tables

SELECT breweries.id, breweries.brewery_name, breweries.city, breweries.state, beer_reviews.review_overall
FROM breweries
JOIN beer_reviews
ON breweries.id = beer_reviews.id;

SELECT beers.id, beers.name, beers.abv, styles.style_name, styles.Glass_Type
FROM beers
JOIN styles
ON beers.style_id = styles.id;

SELECT beers.id, beers.name, beers.abv, categories.cat_name
FROM beers
JOIN categories
ON beers.cat_id = categories.id;