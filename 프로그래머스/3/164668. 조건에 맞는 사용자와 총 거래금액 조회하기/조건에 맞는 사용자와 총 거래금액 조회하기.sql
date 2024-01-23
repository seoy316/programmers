SELECT u.USER_ID, u.NICKNAME, SUM(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD b JOIN USED_GOODS_USER u ON b.WRITER_ID=u.USER_ID
WHERE b.STATUS LIKE "DONE"
GROUP BY u.USER_ID
HAVING SUM(PRICE) >= 700000
ORDER BY TOTAL_SALES ASC;