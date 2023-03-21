import application.db.dbhandler as dbhandler
from application.db.dbhandler import dbValueEnums
from typing import Dict, List, Union
from application.enumtypes import *

def boolControl(value):
    capitalize_val = str(value).lower().capitalize()
    if(capitalize_val == 'True' or capitalize_val == 'False'):
        return True
    else:
        return False

class Variables():
    def __init__(self) -> None:
        pass

    async def _init_(self):
        await dbhandler.createVariablesDb()
        await self.setVariablesFromDb()

    def getVariableValue(self,key):
        attributes = self.__dict__
        try:
            return attributes[key]
        except:
            return None

    async def setVariablesFromDb(self):
        attributes = self.__dict__
        try:
            for id in range(1,136):
                row = await dbhandler.getVariableFromDbById(id)
                print(row)
                if(row[1] == "bool"):
                    attributes[row[0]] = eval(row[2])
                else:
                    attributes[row[0]] = row[2]
        except Exception as e:
            print(e)

    async def setVariable(self,key,value,dataType):
        attributes = self.__dict__
        if(dataType == "bool"):
            attributes[key] = eval(value)
        else:
            attributes[key] = value        
        await dbhandler.updateVariableInDb(key,value)

    async def getAttributeValue(self,variable):
        componantName = variable["component"]["name"]
        variableName = variable["variable"]["name"]
        try:
            componentInstance = variable["component"]["instance"]
        except:
            componentInstance = None
        try:
            variableInstance = variable["variable"]["instance"]
        except:
            variableInstance = None
        variableDict = {"componentName":componantName,"variableName":variableName,"variableInstance":variableInstance}
        ret = await dbhandler.selectVariableFromDb(variableDict)#ret contains id,ocppName,componentName,variableName,variableInstance,dataType,mutability,value
        if ret is None:
            return (None,GetVariableStatusEnumType.UnknownVariable) #TODO check for unkown component or variable
        mutability = ret[dbValueEnums.mutability]
        if(mutability == 'WriteOnly'):
            return (None,GetVariableStatusEnumType.Rejected)
        value = ret[dbValueEnums.value]
        return (value,GetVariableStatusEnumType.Accepted) #value
    
    async def checkAttributeStatus(self,variable,value):
        componantName = variable["component"]["name"]
        variableName = variable["variable"]["name"]
        try:
            componentInstance = variable["component"]["instance"]
        except:
            componentInstance = None
        try:
            variableInstance = variable["variable"]["instance"]
        except:
            variableInstance = None
        variableDict = {"componentName":componantName,"variableName":variableName,"variableInstance":variableInstance}
        ret = await dbhandler.selectVariableFromDb(variableDict) #ret contains id,ocppName,componentName,variableName,variableInstance,dataType,mutability,value
        if ret is None:
            return "UnknownVariable" #TODO check for unkown component or variable
        if(ret[dbValueEnums.mutability] == "ReadOnly"):
            return "Rejected"
        else:
            if(ret[dbValueEnums.dataType] == "int" and isinstance(value,int)):
                print("set value",ret[1],value)
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "bool" and boolControl(value)):
                print("type of value",type(ret[dbValueEnums.value]),type(eval(value)))
                print("set value",ret[dbValueEnums.ocppName],eval(value))
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "str" and isinstance(value,str)):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "DateTime"):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "MemberList"):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "SequenceList"):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "OptionList"):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            elif(ret[dbValueEnums.dataType] == "passwordString"):
                await self.setVariable(ret[dbValueEnums.ocppName],value,ret[dbValueEnums.dataType])
                return "Accepted"
            else:
                return "Rejected"