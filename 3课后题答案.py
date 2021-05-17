from beem.steem import Steem
from beembase import operations
from beem.transactionbuilder import TransactionBuilder
import time
import requests

nodes="https://api.justyy.com"
player="nutbox.awesome"
keys="5KtH7"

data = {"jsonrpc": "2.0", "method": "condenser_api.get_accounts", "params": [[player]], "id": 1}
response = requests.post(url=nodes, json=data)
result = response.json()["result"]
myname=result[0]["name"]
print(myname)

s = Steem(keys=[keys],node=nodes)
id_name="learning"
json_data = {"type": "learning","data":{"myname":myname,"round":1}}
op = operations.Custom_json(
            **{
                "json": json_data,
                "required_auths": [],
                "required_posting_auths": [player],
                "id": id_name,
            })

tx = TransactionBuilder(steem_instance=s)
tx.appendOps(op)
#把签名添加
tx.appendSigner(player, "posting")
print("1生成信息",tx)
tx.sign()
print("2签名信息",tx)
print("3广播信息")
broadcast=tx.broadcast()
print(broadcast)
