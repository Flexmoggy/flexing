steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE profile (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(50) NOT NULL,
            picture_url VARCHAR,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            skills VARCHAR (1000),
            interests VARCHAR (1000),
            bio TEXT
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE user;
        """
    ]
]