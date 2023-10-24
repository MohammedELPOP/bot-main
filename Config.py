import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 24494495
    API_HASH = "883ba24ab125fb77cdfe6fb54408c569"
    BOT_TOKEN = "6859156795:AAH8IDaYPfFn2vf-x2wsJOFkI8pnbxPCQ2o"
    DATABASE_URL = "postgres://dvvxiyxi:qb6Vy-yTtCo0fn6Ios3CjSd1q_CWJcDC@peanut.db.elephantsql.com/dvvxiyxi"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "sw_vx"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
