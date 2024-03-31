CREATE or ALTER VIEW [Poke] 
AS 
SELECT [ID]
      ,[Name]
	  ,[ID_Name]
      --,[Name_EN]
      ,[Genus]
      --,[Genus_EN]
      ,[Forme]
      ,[Type1_D] AS Type1
      ,[Type2_D] AS Type2
      --,[Type1_EN_D] AS Type1_EN
      --,[Type2_EN_D] AS Type2_EN
      ,[Species Strength]
	  ,[HP]
      ,[Atk]
      ,[Def]
      ,[Sp# Atk] AS [Sp Atk]
      ,[Sp# Def] AS [Sp Def]
      ,[Speed]
      ,[Desc]
      --,[Desc_EN]
  FROM [WF_DB].[dbo].[Pokemon_Data]
 GO

SELECT * FROM [Poke]
    ORDER BY ID
