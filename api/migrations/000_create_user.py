steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE user (
            id SERIAL PRIMARY KEY NOT NULL,
            email VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE user;
        """
    ]
]
