SELECT a.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM (
    SELECT *
    FROM BOOK_SALES
    WHERE SALES_DATE LIKE '2022-01-%' 
) s LEFT JOIN BOOK b ON b.BOOK_ID = s.BOOK_ID
    LEFT JOIN AUTHOR a ON b.AUTHOR_ID = a.AUTHOR_ID
GROUP BY a.AUTHOR_ID, AUTHOR_NAME, CATEGORY
ORDER BY a.AUTHOR_ID ASC, CATEGORY DESC;