cost_of_asset = float(input("Enter the cost of the asset: "))

salvage_value = float(input("Enter the salvage value of the asset: "))

useful_life = int(input("Enter the useful life of the asset (in years): "))

annual_depreciation = (cost_of_asset - salvage_value) / useful_life

print(f"The annual depreciation of the asset is: {annual_depreciation}")
