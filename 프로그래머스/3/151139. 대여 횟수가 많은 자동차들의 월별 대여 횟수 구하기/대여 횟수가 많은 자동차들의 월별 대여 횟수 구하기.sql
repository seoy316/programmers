select extract(month from start_date) as month,
       car_id,
       count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
    select car_id
     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
     where start_date between to_date('2022-08-01', 'YYYY-MM-DD') 
                            and to_date('2022-10-31', 'YYYY-MM-DD')
     group by car_id
     having count(*) >= 5)
 and start_date between to_date('2022-08-01', 'YYYY-MM-DD') 
                            and to_date('2022-10-31', 'YYYY-MM-DD')
group by extract(month from start_date), car_id
order by month asc, car_id desc