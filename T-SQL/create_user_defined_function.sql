CREATE or ALTER FUNCTION Get_Max_Strength_Poke 
(@Type_Text NVARCHAR(20)=null)
RETURNS INT
AS

BEGIN
	RETURN(
		Select MAX([Species Strength]) from [Poke] 
		Where ([Type1] like '%' + IsNull(@Type_Text,[Type1]) + '%') or ([Type2] like '%' + IsNull(@Type_Text,[Type2]) + '%')
	)
END

GO

------https://stackoverflow.com/questions/8358315/t-sql-function-with-default-parameters----

----Method 1
select dbo.Get_Max_Strength_Poke(default) AS num1, dbo.Get_Max_Strength_Poke('¤õ') AS num2
----When a parameter of the function has a default value, the keyword DEFAULT must be specified when the function is called in order to retrieve the default value. This behaviour is different from using parameters with default values in stored procedures in which omitting the parameter also implies the default value. An exception to this behaviour is when invoking a scalar function by using the EXECUTE statement. When using EXECUTE, the DEFAULT keyword is not required.
GO

----Method 2
DECLARE @N1  INT,  @N2  INT;
EXEC @N1 = Get_Max_Strength_Poke
EXEC @N2 = Get_Max_Strength_Poke '¤õ'
SELECT @N1 AS num1, @N2 AS num2
GO