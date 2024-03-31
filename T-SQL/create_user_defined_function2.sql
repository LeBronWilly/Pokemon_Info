CREATE or ALTER FUNCTION Get_Max_Strength_Poke_Table
(@Type_Text NVARCHAR(20)=null)
RETURNS TABLE
AS


RETURN(
Select MAX([Species Strength]) as [num1] from [Poke] 
Where ([Type1] like '%' + IsNull(@Type_Text,[Type1]) + '%') or ([Type2] like '%' + IsNull(@Type_Text,[Type2]) + '%')
)


GO


select * from Get_Max_Strength_Poke_Table(default)
select * from Get_Max_Strength_Poke_Table('¤õ')

GO


----Method 2
DECLARE @N1  TABLE(Column1 INT);
INSERT INTO @N1 select * from Get_Max_Strength_Poke_Table(default);
SELECT * FROM @N1

DECLARE @N2  TABLE(Column2 INT);
INSERT INTO @N2 select * from Get_Max_Strength_Poke_Table('¤õ');
SELECT * FROM @N2
GO