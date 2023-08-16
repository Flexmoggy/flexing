## Create the table
steps = [ 
    [
    # CREATE TABLE 
    """
    CREATE TABLE review (
        id SERIAL PRIMARY KEY NOT NULL,
        author INT NOT NULL,
        reviewee INT NOT NULL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        rating INT NOT NULL,
        review_text TEXT
    );
    """,
    # DROP TABLE
    """
    DROP TABLE review;
    """
    ]
]
