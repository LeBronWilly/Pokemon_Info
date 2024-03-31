CREATE or ALTER PROCEDURE sp_Poke 
( @Type_Text nvarchar(20)=null )
AS

--BEGIN
SELECT [ID]
      ,[Name]
	  ,[ID_Name]
      ,[Genus]
      ,[Forme]
      ,[Type1_D] AS Type1
      ,[Type2_D] AS Type2
      ,[Species Strength]
	  ,[HP]
      ,[Atk]
      ,[Def]
      ,[Sp# Atk] AS [Sp Atk]
      ,[Sp# Def] AS [Sp Def]
      ,[Speed]
      ,[Desc]
  FROM [WF_DB].[dbo].[Pokemon_Data]
  WHERE ([Type1] like '%' + IsNull(@Type_Text,[Type1]) + '%') or ([Type2] like '%' + IsNull(@Type_Text,[Type2]) + '%')
  ORDER BY ID
--END

GO

EXEC sp_Poke
EXEC sp_Poke '¤õ'
