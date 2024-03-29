SELECT YEAR(o.SALES_DATE) AS YEAR, 
        MONTH(o.SALES_DATE) AS MONTH, 
        COUNT(DISTINCT i.USER_ID) AS PUCHASED_USERS,
        ROUND(COUNT(DISTINCT i.USER_ID) / (SELECT COUNT(*)
                            FROM USER_INFO 
                            WHERE YEAR(JOINED) = 2021)
              ,1) AS PUCHASED_RATIO
    
FROM USER_INFO i LEFT JOIN ONLINE_SALE o ON i.USER_ID=o.USER_ID
WHERE YEAR(JOINED) = 2021 AND o.online_sale_id IS NOT NULL
GROUP BY YEAR(o.SALES_DATE), MONTH(o.SALES_DATE)
ORDER BY 1, 2