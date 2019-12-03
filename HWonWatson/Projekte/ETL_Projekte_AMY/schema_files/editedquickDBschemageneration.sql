DROP TABLE IF EXISTS beers_reduced_df;
DROP TABLE IF EXISTS breweries_reduced_df;
DROP TABLE IF EXISTS brewery_address;
DROP TABLE IF EXISTS brewery_coordinates;
DROP TABLE IF EXISTS brewery_type;
DROP TABLE IF EXISTS categories_cleaned;
DROP TABLE IF EXISTS contact_brewery;
DROP TABLE IF EXISTS styles_reduced_df;

CREATE TABLE "beers_reduced_df" (
    "id" INTEGER   NOT NULL,
    "name" VARCHAR(30)   NOT NULL,
    "brewery_id" INTEGER   NOT NULL,
    "cat_id" INTEGER   NOT NULL,
    "style_id" INTEGER   NOT NULL,
    "abv" DECIMAL(3,1)   NULL,
    CONSTRAINT "pk_beers_reduced_df" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "breweries_reduced_df" (
    "id" INTEGER   NOT NULL,
    "name" VARCHAR(100)   NOT NULL,
    "address1" VARCHAR(100)   NULL,
    "city" VARCHAR(30)   NOT NULL,
    "state" VARCHAR(30)   NOT NULL,
    "country" VARCHAR(30)   NOT NULL,
    "phone" VARCHAR(20)   NULL,
    "website" VARCHAR(100)   NULL,
    CONSTRAINT "pk_breweries_reduced_df" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "categories_cleaned" (
    "id" INTEGER   NOT NULL,
    "cat_name" VARCHAR(30)   NOT NULL,
    CONSTRAINT "pk_categories_cleaned" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "styles_reduced_df" (
    "id" INTEGER   NOT NULL,
    "cat_id" INTEGER   NOT NULL,
    "style_name" VARCHAR(75)   NOT NULL,
    "ABV_Low" DECIMAL(3,1)   NULL,
    "ABV_High" DECIMAL(3,1)   NULL,
    "Glass_Type" VARCHAR(20)   NULL,
    CONSTRAINT "pk_styles_reduced_df" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "brewery_type" (
    "id" INTEGER  NOT NULL,
    "name" VARCHAR(100)   NOT NULL,
    "brewery_type" VARCHAR(10)   NOT NULL,
	CONSTRAINT "pk_brewery_type" PRIMARY KEY ("id")
     );

CREATE TABLE "contact_brewery" (
    "id" INTEGER   NOT NULL,
    "name" VARCHAR (100)  NOT NULL,
    "phone" VARCHAR(20)   NULL,
    "website_url" VARCHAR(100)   NULL
);

CREATE TABLE "brewery_address" (
    "id" INTEGER   NOT NULL,
    "street" VARCHAR(100)   NULL,
    "city" VARCHAR(30)   NULL,
    "state" VARCHAR(30)   NULL,
    "country" VARCHAR(30)   NULL
);

CREATE TABLE "brewery_coordinates" (
    "id" INTEGER   NOT NULL,
    "latitude" DECIMAL(9,6)   NULL,
    "longitude" DECIMAL(9,6)   NULL
);

ALTER TABLE "beers_reduced_df" ADD CONSTRAINT "fk_beers_reduced_df_brewery_id" FOREIGN KEY("brewery_id")
REFERENCES "breweries_reduced_df" ("id");

ALTER TABLE "beers_reduced_df" ADD CONSTRAINT "fk_beers_reduced_df_cat_id" FOREIGN KEY("cat_id")
REFERENCES "categories_cleaned" ("id");

ALTER TABLE "beers_reduced_df" ADD CONSTRAINT "fk_beers_reduced_df_style_id" FOREIGN KEY("style_id")
REFERENCES "styles_reduced_df" ("id");

ALTER TABLE "styles_reduced_df" ADD CONSTRAINT "fk_styles_reduced_df_cat_id" FOREIGN KEY("cat_id")
REFERENCES "categories_cleaned" ("id");

ALTER TABLE "contact_brewery" ADD CONSTRAINT "fk_contact_brewery_id_name" FOREIGN KEY("id")
REFERENCES "brewery_type" ("id");

ALTER TABLE "brewery_address" ADD CONSTRAINT "fk_brewery_address_id" FOREIGN KEY("id")
REFERENCES "brewery_type" ("id");

ALTER TABLE "brewery_coordinates" ADD CONSTRAINT "fk_brewery_coordinates_id" FOREIGN KEY("id")
REFERENCES "brewery_type" ("id");