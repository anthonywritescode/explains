WITH RECURSIVE nn (i, o) AS (
    SELECT 1, '1'
    UNION ALL
    SELECT
        nn.i + 1,
        CASE
            WHEN (nn.i + 1) % 15 = 0 THEN 'fizzbuzz'
            WHEN (nn.i + 1) % 3 = 0 THEN 'fizz'
            WHEN (nn.i + 1) % 5 = 0 THEN 'buzz'
            ELSE (nn.i + 1)
        END
    FROM nn
    WHERE nn.i < 30
)
SELECT i, o FROM nn;
