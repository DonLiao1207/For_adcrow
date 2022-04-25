/**
    • 1.Query users (name) who have a bigger deposit than their agent
    • 2.Query users (name) who have the biggest deposit in their region
    • 3.Query the third highest deposit of users
**/

/*1.*/
select name from
(select name, agent_id , deposit  from users as tbl1 
left join 
(select user_id as user_agent, deposit as ag_depo from users where agent_id is null) as tbl2 
on tbl1.agent_id = tbl2.user_agent 
where agent_id is not null and  int8(tbl1.deposit) - int8(tbl2.ag_depo) >= 1) as bigger_than_agent;
/*2.*/
select name from
(select name, deposit, tbl2.max_in_region from users as tbl1
left join
(select region, max(deposit) as max_in_region from users group by region) as tbl2 
on tbl1.deposit = tbl2.max_in_region
where tbl2.max_in_region is not null) as region_biggest_deposit;
/*3.*/
WITH RESULT AS  
(  
    SELECT deposit ,  
           DENSE_RANK() OVER (ORDER BY deposit DESC) AS DENSERANK  
    FROM users u  
)  
SELECT deposit 
FROM RESULT  
WHERE DENSERANK = 3






