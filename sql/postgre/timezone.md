# [timezone](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-ZONECONVERT)
- https://blog.billo.io/devposts/psql_at_time_zone/

### postgresql timezone 표현
- `TIMESTAMP WITHOUT TIME ZONE AT TIME ZONE zone` 형태로, timestamp without time zone을 해당 zone에서의 timestamp라고 생각하고, timestamp with time zone 값을 반환한다.    
- `TIMESTAMP WITH TIME ZONE AT TIME ZONE zone` 형태로, timestamp with time zone 값을 해당 zone에서의 timestamp without time zone 값을 반환한다.    

### [timezone 형태](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-TIMEZONES)
- Asia/Seoul형태의 Timezone full name
- PST형태의 줄임말
- POSIX-Style의 Timezone 표기법인 STDoffset, STDoffsetDST (DST는 일광절약시간) 형태. e.g. KST5, EDT5DST  
> UTC+9 형태로 표시하면 3번에 해당하게 되는데, 이 POSIX-Style에서 offset을 일반적으로 세는 방향과 반대인 `numeric offset in hours west from UTC` 즉 `UTC로부터 서쪽으로 시간상 얼마나 떨어져 있는지`를 세고 있던 것이다. 우리가 알고있는 UTC+9의 형태는 동쪽으로 계산한 값이다. 따라서 `AT TIME ZONE 'UTC+9'` 는 우리나라랑은 그리니치 천문대 기준으로 대칭적인 위치의 시간대에 해당하는 값이어서, 값이 이상하게 나왔던 것이다.


### 타임존 변경
```sql
-- A at time zone 변경하고 싶은 타임존(또는 offset) at time zone A의 타임존(또는 offset)  
select
  t1.start_dt::timestamp at time zone t1.dt_time_zone at time zone 'utc' as target_dt
from tb t1
where 1=1
; 
```
### timezone
```sql
show timezone;

select timestamp '2020-08-06 12:00:00' at time zone 'Asia/Seoul';
select timestamp '2020-08-06 12:00:00' at time zone 'utc+9';
```
### timezone table
```sql
select * from pg_timezone_names where abbrev='KST';
```

