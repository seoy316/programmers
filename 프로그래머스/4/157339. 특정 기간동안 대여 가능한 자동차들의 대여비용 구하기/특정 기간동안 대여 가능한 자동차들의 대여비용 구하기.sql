SELECT c.car_id, c.car_type,
       FLOOR(c.daily_fee * 30 * (1 - p.discount_rate/100)) fee
FROM CAR_RENTAL_COMPANY_CAR c
INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p
ON c.car_type = p.car_type
LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h 
ON c.car_id = h.car_id
   AND h.end_date >= '2022-11-01' AND h.start_date <= '2022-11-30'
WHERE ROUND(c.daily_fee * 30 * (1 - p.discount_rate/100)) BETWEEN 500000 AND 1999999
        AND h.car_id IS NULL
        AND p.duration_type = '30일 이상'
        AND c.car_type IN ('SUV', '세단')
ORDER BY fee DESC, c.car_type, c.car_id DESC;