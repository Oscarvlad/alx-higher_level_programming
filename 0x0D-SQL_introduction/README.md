# 0x0D. SQL - Introduction

<code>0-privileges.sql:</code> <p>Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).</p>

<code>1-create_user.sql:</code> <p>Write a script that creates the MySQL server user user_0d_1.</p>
<ul>
    <li>user_0d_1 should have all privileges on your MySQL server</li>
    <li>The user_0d_1 password should be set to user_0d_1_pwd</li>
    <li>If the user user_0d_1 already exists, your script should not fail</li>
</ul>

<code>2-create_read_user.sql:</code> <p>Write a script that creates the database hbtn_0d_2 and the user user_0d_2.</p>
<ul>
	<li>user_0d_2 should have only SELECT privilege in the database hbtn_0d_2</li>
 	<li>The user_0d_2 password should be set to user_0d_2_pwd</li>
 	<li>If the database hbtn_0d_2 already exists, your script should not fail</li>
 	<li>If the user user_0d_2 already exists, your script should not fail</li>
</ul>

<code>3-force_name.sql:</code> <p>Write a script that creates the table force_name on your MySQL server.</p>
<lu>
	<li>force_name description:</li>
        <li>id INT</li>
	<li>name VARCHAR(256) can’t be null</li>
    	<li>The database name will be passed as an argument of the mysql command</li>
    	<li>If the table force_name already exists, your script should not fail</li>
</lu>

<code>4-first_table.sql:</code> <p>Write a script that creates a table called first_table in the current database in your MySQL server.</p>
<lu>
	<li>first_table description:</li>
 	<li>id INT</li>
   	<li>name VARCHAR(256)</li>
	<li>The database name will be passed as an argument of the mysql command</li>
 	<li>If the table first_table already exists, your script should not fail</li>
 	<li>You are not allowed to use the SELECT or SHOW statements</li>
</lu>

<code>5-full_table.sql:</code> <p>Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.</p>
<lu>
	<li>The database name will be passed as an argument of the mysql command</li>
	<li>You are not allowed to use the DESCRIBE or EXPLAIN statements</li>
</lu>

<code>6-list_values.sql:</code> <p>Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.</p>
<lu>
	<li>All fields should be printed</li>
	<li>The database name will be passed as an argument of the mysql command</li>
</lu>

<code>7-insert_value.sql:</code> <p>Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.</p>
<lu>
	<li>id = 89</li>
	<li>name = Best School</li>
	<li>The database name will be passed as an argument of the mysql command</li>
</lu>

<code>8-count_89.sql:</code> <p>Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.</p>
<lu>
	<li>The database name will be passed as an argument of the mysql command</li>
</lu>

<code>9-full_creation.sql:</code> <p>Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.</p>

<li><code>second_table</code> description:

<ul>
<li><code>id</code> INT</li>
<li><code>name</code> VARCHAR(256)</li>
<li><code>score</code> INT</li>
</ul></li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>
<li>If the table <code>second_table</code> already exists, your script should not fail</li>
<li>You are not allowed to use the <code>SELECT</code> and <code>SHOW</code> statements</li>
<li>Your script should create these records:

<ul>
<li><code>id</code> = 1, <code>name</code> = “John”, <code>score</code> = 10</li>
<li><code>id</code> = 2, <code>name</code> = “Alex”, <code>score</code> = 3</li>
<li><code>id</code> = 3, <code>name</code> = “Bob”, <code>score</code> = 14</li>
<li><code>id</code> = 4, <code>name</code> = “George”, <code>score</code> = 8</li>
</ul></li>

<code>10-top_score.sql:</code>
<p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first) </li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>

<code>11-best_score.sql:</code>
<p>Write a script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<li>Results should display both the score and the name (in this order)</li>
<li>Records should be ordered by score (top first)</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>

<code>12-no_cheating.sql:</code>
<p>Write a script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>
<li>You are not allowed to use Bob’s id value, only the <code>name</code> field</li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>

<code>13-change_class.sql</code>
<p>Write a script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>

<code>14-average.sql:</code>
<p>Write a script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<li>The result column name should be <code>average</code></li>
<li>The database name will be passed as an argument of the <code>mysql</code> command</li>

<code>15-groups.sql:</code>
<p>Write a script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>
<li>The result should display:
<ul>
<li>the <code>score</code></li>
<li>the number of records for this <code>score</code> with the label <code>number</code></li>
</ul></li>
<li>The list should be sorted by the number of records (descending)</li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>

<code>16-no_link.sql:</code>
<p>Write a script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>

<li>Don’t list rows without a <code>name</code> value</li>
<li>Results should display the score and the name (in this order)</li>
<li>Records should be listed by descending score </li>
<li>The database name will be passed as an argument to the <code>mysql</code> command</li>

