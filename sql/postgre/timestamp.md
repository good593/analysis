# Timestamp
- https://m.blog.naver.com/sssang97/222054185948

### 시간 타입
> postgresql의 시간 관리용 티입으로는 timestamp, date, time 등이 있다.  

### 시간값 획득하기
- NOW() (= current_timestamp)
```sql
select now();
select pg_typeof(now());  -- 타임스탬프에 타임존이 합쳐진 값을 반환
```
- current_time
```sql
select current_time;
```
- current_date
```sql
select current_date;
```

### 변환
```sql
select to_char(now(), 'YYYY-MM-DD HH24');
select now()::Date;
select (now()::Date)::timestamp;
select now()::time;

-- 유닉스
select extract(epoch from now());
select extract(epoch from now())::integer;
select to_timestamp(1596793575);
```
### 시간 계산
```sql
select interval '1 day'; -- year, month, day, hour, minute, second 등
select now() - interval '10 day';
select now() + interval '10 year';

select (now()) - (now() - interval '10 year');
select age(now(), now() - interval '10 year');
```
### 시간 부분값 추출: extract
```sql
select extract(day from now());
select extract(year from now());
```
### 시간값 내림: date_trunc
```sql
select date_trunc('minute', now());
select date_trunc('hour', now());
select date_trunc('day', now());
```


