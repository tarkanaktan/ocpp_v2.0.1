import asyncio
import json

from ocpp.websocket.websocketProtocol import WebSocket
from application.myChargePoint import MyChargePoint
from application.db.variables import Variables

import ocpp.ocppmessages.incomingmessages as incomingmessages
from application.enumtypes import *
from dataclasses import asdict


async def main():
    configurationSlot = 1
    connectionData = incomingmessages.ConnectionData(ocppVersion=OCPPVersionEnumType.OCPP20,ocppTransport=OCPPTransportEnumType.JSON,ocppCsmsUrl="ws://localhost:9000/CP_1",messageTimeout=30,securityProfile=0,ocppInterface=OCPPInterfaceEnumType.Wired0)
    uriList=[]
    uriList.append(str(asdict(connectionData)))
    print(uriList,type(uriList),isinstance(uriList,list))
    variables = Variables()
    await variables._init_()
    variables.NetworkConfigurationPriority= variables.NetworkConfigurationPriority.split(",")
    print("NetworkConfigurationPriority",variables.NetworkConfigurationPriority,type(variables.NetworkConfigurationPriority))
    connectionDataFromDb = await variables.getNetworkProfile(variables.NetworkConfigurationPriority[0])
    if connectionDataFromDb is not None:
        connectionData_json = json.loads(connectionDataFromDb)
        print(connectionData_json["ocppCsmsUrl"])
        uri = connectionData_json["ocppCsmsUrl"]
    else:
        uri = '''ws://localhost:7000/CP1'''
    #await variables.putNetworkProfile(configurationSlot,str(asdict(connectionData)))
    #await variables.setVariable("NetworkConfigurationPriority",uriList,"SequenceList")
    while(True):
        try:
            connection = WebSocket(uri=uri, subprotocols=["ocpp2.0.1"], ping_interval=None, ping_timeout=None)
            async with connection.connect() as client:
                chargePoint = MyChargePoint("CP_1",client,variables,uriList)
                chargePoint.setConnectorCount(2)
                chargePoint.createEvseObject()
                await asyncio.gather(
                    chargePoint.start(), chargePoint.startProcedure()
                )
        except:
            print("try again")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
