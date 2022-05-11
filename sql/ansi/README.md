# ANSI (American National Standards Institute; 미국표준협희)  
- https://velog.io/@gillog/ANSI-SQL%EC%9D%B4%EB%9E%80
- https://easybrother0103.tistory.com/137
- https://dejavuhyo.github.io/posts/ansi-sql/

## 특징
- 장점
  - 표준 SQL 문법이기 때문에 거의 대부분 DBMS에서 작동이 가능합니다.  
  - 표준 SQL문이기 때문에 DBMS의 종류에 제약을 받지 않는다. 즉, DBMS에 종속적이지 않아 DBMS를 변경하더라도 쉽게 이동할 수 있다.     
  - 테이블간의 Join 관계가 FROM 에서 명시되기 때문에 WHERE 문에서 조건만 확인하면 된다. 즉, 가독성이 좋다.   
- 단점
  - DBMS 내부의 함수를 사용하는 경우 ANSI 문법만으로 쿼리 작성이 불가능한 경우가 있다.  

## SQL example  
### 1 Inner Join / join
```sql
-- 테이블 2개 조인
select
  tb1.*
  , tb2.name
from tb1 inner join tb2
  on (tb1.id = tb2.id and tb1.num = tb2.num)
where 1=1
;
-- 테이블 3개 이상 조인
select
  t1.name
  , t2.age
  , t3.address
from tb1 t1
join tb2 t2
  on t1.id = t2.id
join tb3 t3
  on t2.id = t3.id
where t1.name is not null
;
```
### 2 Outer Join
#### 2-1 Left Outer Join / Left Join
- from 절에 left outer join을 명시해주면 된다.  
- 왼쪽 테이블을 기준으로 데이터가 출력되고 조건에 맞는 오른쪽 테이블의 컬럼이 같이 출력된다.  
- 왼쪽 테이블은 전체가 출력되므로, 오른쪽 테이블에 참조할 값이 없으면 null이 나온다.  
- 만약 조건에 맞는 오른쪽 컬럼 값이 다수인 경우 오른쪽 컬럼이 여러개 출력된다.  
```sql
select 
  tb1.*
  , tb2.name
from tb1 left join tb2
  on tb1.num = tb2.num
where 1=1
;
```
#### 2-2 Right Outer Join / Right Join
- from 절에 right outer join을 명시해주면 된다.
- 오른쪽 테이블을 기준으로 데이터가 출력되고 조건에 맞는 왼쪽 테이블의 컬럼이 같이 출력된다.  
- 오른쪽 테이블은 전체가 출력되므로, 왼쪽 테이블에 참조할 값이 없으면 null이 나온다.
- 만약 조건에 맞는 왼쪽 컬럼 값이 다수인 경우 왼쪽 컬럼이 여러개 출력된다.
```sql
select
  tb1.*
  , tb2.name
from tb1 right join tb2
  on tb1.num = tb2.num
where 1=1
;
```
#### 2-3 Full Outer Join
- ANSI에서만 지원하며, Left Outer Join과 Right Outer Join을 합친 것으로, 양쪽 모두 조건이 일치하지 않는 것까지 모두 결합해 출력한다.  
```sql
select 
  tb1.*
  , tb2.name
from tb1 full outer join tb2
  on tb1.num = tb2.num
where 1=1
;
```




