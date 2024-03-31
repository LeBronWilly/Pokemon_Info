CREATE or ALTER PROCEDURE sp_Get_Max_Max_Strength_Type_Poke 
( @Type_Text nvarchar(20)=null, @strength int=null)
AS

BEGIN
	----https://www.c-sharpcorner.com/blogs/call-a-function-in-stored-procedure1
	----https://jengting.blogspot.com/2014/02/user-define-function.html
	----https://hackmd.io/@Not/MSSQLStoredProcedureIntro
	DECLARE @max_strength nvarchar(20)
	SET @max_strength = dbo.Get_Max_Strength_Poke(@Type_Text)

	SELECT * FROM [Poke] 
	WHERE 
		(([Type1] like '%' + IsNull(@Type_Text,[Type1]) + '%') or ([Type2] like '%' + IsNull(@Type_Text,[Type2]) + '%')) and 
		([Species Strength]=@max_strength)
	order by [ID]
END

GO




EXEC sp_Get_Max_Max_Strength_Type_Poke '¤ô'
--EXEC sp_Get_Max_Max_Strength_Type_Poke @Type_Text='¤õ'

EXEC sp_Get_Max_Max_Strength_Type_Poke
--EXEC sp_Get_Max_Max_Strength_Type_Poke default
--EXEC sp_Get_Max_Max_Strength_Type_Poke @Type_Text=default
GO