-- 코드를 입력하세요
-- first_half = 상반기
-- icecream_info = 성분표
SELECT f.FLAVOR
from FIRST_HALF f
join ICECREAM_INFO i
on f.FLAVOR = i.FLAVOR
WHERE f.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE = 'fruit_based'
order by f.TOTAL_ORDER desc;