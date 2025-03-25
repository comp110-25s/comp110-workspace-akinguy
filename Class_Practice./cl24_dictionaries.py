"""Examples of set and dictionary syntax"""

pids: set[int] = {710000000, 712345678}
pids.add(730710295)


ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 10,
    "strawberry": 5,
}
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

ice_cream["vanilla"] += 110

for flavor in ice_cream:
    print(flavor)
    print(ice_cream[flavor])
