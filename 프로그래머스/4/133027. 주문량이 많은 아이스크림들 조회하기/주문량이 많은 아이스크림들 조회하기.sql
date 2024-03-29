WITH ICE AS (
    SELECT *
    FROM FIRST_HALF 
    UNION ALL
    SELECT * 
    FROM JULY
)

SELECT FLAVOR 
FROM (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM ICE
    GROUP BY FLAVOR
) AS f
ORDER BY TOTAL_ORDER DESC
LIMIT 3;
