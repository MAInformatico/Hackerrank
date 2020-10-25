select h.hacker_id, name, sum(score) as total_score
from hackers as h inner join (select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score on h.hacker_id=max_score.hacker_id group by h.hacker_id, name having total_score > 0 order by total_score desc, h.hacker_id;
