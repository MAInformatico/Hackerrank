Select distinct city from station where REGEXP_LIKE(City, '^[^AEIOU].*[^aeiou]$');
