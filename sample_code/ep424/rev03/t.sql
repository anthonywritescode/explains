WITH RECURSIVE nn (i) AS (
    SELECT 1
    UNION ALL
    SELECT nn.i + 1
    FROM nn
    WHERE nn.i < 30
)
SELECT
    nn.i,
    CASE
        WHEN nn.i % 15 = 0 THEN 'fizzbuzz'
        WHEN nn.i % 3 = 0 THEN 'fizz'
        WHEN nn.i % 5 = 0 THEN 'buzz'
        ELSE nn.i
    END
FROM nn;
