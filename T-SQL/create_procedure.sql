CREATE or ALTER PROCEDURE sp_Get_Type_Poke 
( @Type_Text nvarchar(20)=null )
AS

--BEGIN
	SELECT * FROM [Poke] 
	WHERE ([Type1] like '%' + IsNull(@Type_Text,[Type1]) + '%') or ([Type2] like '%' + IsNull(@Type_Text,[Type2]) + '%')
	----Type1 like '%'+IsNull(@Type_Text,[Type1])+'%' will return all records if @Type_Text param is null
	order by [ID]
--END

GO


EXEC sp_Get_Type_Poke '¤õ'
--EXEC sp_Get_Type_Poke @Type_Text='¤õ'

EXEC sp_Get_Type_Poke
--EXEC sp_Get_Type_Poke default
--EXEC sp_Get_Type_Poke @Type_Text=default
GO