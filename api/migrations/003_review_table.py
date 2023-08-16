## Create the table
steps = [ 
    [
    # CREATE TABLE 
    """
    CREATE TABLE reviews (
        id SERIAL PRIMARY KEY NOT NULL,
        reviewer INT NOT NULL,
        reviewee INT NOT NULL,
        datetime VARCHAR(255),
        rating INT ,
        review TEXT,
        CHECK (rating >= 1 AND rating <= 5)
    );
    """,
    # DROP TABLE
    """
    DROP TABLE reviews;
    """
    ]
]
