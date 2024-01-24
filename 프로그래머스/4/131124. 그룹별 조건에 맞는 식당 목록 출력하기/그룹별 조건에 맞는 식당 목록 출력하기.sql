SELECT MEMBER_NAME, REVIEW_TEXT,DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE p JOIN REST_REVIEW r ON p.MEMBER_ID = r.MEMBER_ID
WHERE p.MEMBER_ID = (
    SELECT MEMBER_ID
    FROM REST_REVIEW 
    GROUP BY MEMBER_ID
    ORDER BY COUNT(MEMBER_ID) DESC
    LIMIT 1
)
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC