steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE event (
            id SERIAL PRIMARY KEY NOT NULL,
            topic VARCHAR(50) NOT NULL,
            author VARCHAR(50),
            partner VARCHAR(50),
            paired BOOLEAN NOT NULL DEFAULT FALSE,
            expired BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            zoom_link VARCHAR(500),
            category VARCHAR(100),
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE event;
        """
    ]
]
