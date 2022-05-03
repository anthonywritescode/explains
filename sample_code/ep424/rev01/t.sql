WITH RECURSIVE nn (i) AS (
    SELECT 1
    UNION ALL
    SELECT nn.i + 1
    FROM nn
    WHERE nn.i < 30
)
SELECT * FROM nn;
