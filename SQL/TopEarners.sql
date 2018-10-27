select * from (select max(months*salary), count(employee_id) from employee group by months*salary order by months*salary desc) where rownum = 1;
