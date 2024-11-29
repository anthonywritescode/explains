import psycopg2


def main():
    for _ in range(10000):
        psycopg2.connect("user=postgres host=127.0.0.1 dbname=sentry").close()


main()
