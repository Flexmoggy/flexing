steps = [
    [
        # username field will need a Foreign Key relation to the user table,
        # lets not forget to put that in before making a final push.

        # dont forget to edit this file and the API endpoints
        # to match any new tables we create.


        # "Up" SQL statement
        """
        CREATE TABLE profile (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(50) NOT NULL,
            picture_url VARCHAR,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            skills VARCHAR (1000),
            interests VARCHAR (1000),
            bio TEXT
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE profile;
        """
    ]
]
