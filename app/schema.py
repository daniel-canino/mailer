instructions = [
    'DROP TABLE IF EXISTS email;',
    """
        CREATE TABLE email(
            id SERIAL PRIMARY KEY,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL 
        )
    """
]