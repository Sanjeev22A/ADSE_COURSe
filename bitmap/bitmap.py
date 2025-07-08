from typing import Any,Dict,List
##Field description here
fields = {
    "id": {
        "type": "integer",
        "category": "unique identifier",
        "description": "Unique row identifier, typically auto-incremented"
    },
    "gender": {
        "type": "string",
        "category": "categorical",
        "description": "Gender of the individual, e.g., 'M', 'F', or 'Other'"
    },
    "region": {
        "type": "string",
        "category": "categorical",
        "description": "Geographical region, e.g., 'US', 'EU', 'Asia'"
    },
    "age": {
        "type": "integer",
        "category": "continuous",
        "description": "Age of the individual in years"
    },
    "income": {
        "type": "float",
        "category": "continuous",
        "description": "Annual income in USD"
    },
    "education": {
        "type": "string",
        "category": "categorical",
        "description": "Education level, e.g., 'High School', 'Bachelor', 'Master', 'PhD'"
    },
    "married": {
        "type": "string",
        "category": "categorical",
        "description": "Marital status: 'Yes' or 'No'"
    },
    "height_cm": {
        "type": "float",
        "category": "continuous",
        "description": "Height of the person in centimeters"
    },
    "device_type": {
        "type": "string",
        "category": "categorical",
        "description": "Device used: 'mobile', 'desktop', 'tablet', etc."
    },
    "purchase_amt": {
        "type": "float",
        "category": "continuous",
        "description": "Total amount spent in the last purchase"
    }
}

##Fields present

column_lst=["id","gender","region","age","device_type","purchase_amt"]

##Dataset here

dataset = [
    {
        "id": 0,
        "gender": "M",
        "region": "US",
        "age": 25,
        "device_type": "mobile",
        "purchase_amt": 120.5
    },
    {
        "id": 1,
        "gender": "F",
        "region": "EU",
        "age": 30,
        "device_type": "desktop",
        "purchase_amt": 250.0
    },
    {
        "id": 2,
        "gender": "F",
        "region": "US",
        "age": 22,
        "device_type": "tablet",
        "purchase_amt": 90.0
    },
    {
        "id": 3,
        "gender": "M",
        "region": "Asia",
        "age": 45,
        "device_type": "mobile",
        "purchase_amt": 320.0
    },
    {
        "id": 4,
        "gender": "F",
        "region": "EU",
        "age": 27,
        "device_type": "mobile",
        "purchase_amt": 130.0
    },
    {
        "id": 5,
        "gender": "M",
        "region": "US",
        "age": 33,
        "device_type": "desktop",
        "purchase_amt": 210.0
    },
    {
        "id": 6,
        "gender": "F",
        "region": "Asia",
        "age": 29,
        "device_type": "tablet",
        "purchase_amt": 180.0
    },
    {
        "id": 7,
        "gender": "M",
        "region": "Africa",
        "age": 35,
        "device_type": "mobile",
        "purchase_amt": 75.0
    },
    {
        "id": 8,
        "gender": "F",
        "region": "EU",
        "age": 41,
        "device_type": "desktop",
        "purchase_amt": 300.0
    },
    {
        "id": 9,
        "gender": "M",
        "region": "US",
        "age": 24,
        "device_type": "tablet",
        "purchase_amt": 110.0
    }
]

class BitMapGenerationException(Exception):
    ##Throw this exception when trying to create bitmap on continious data
    pass

##This will store the bitmap indexes as fieldname:bitmap
bitmap_collection={}

def generate_bit_map(field:Any):
    field_des=fields.get(field)
    if(field not in column_lst):
        raise BitMapGenerationException(f"The field:{field} isnt a valid field")
    if(field_des['category']!='categorical'):
        raise BitMapGenerationException(f"The field :{field} isnt categorical")
    
    field_entry_set=set()
    for row in dataset:
        field_entry_set.add(row.get(field))
    
    bitmap={}
    for val in field_entry_set:
        cur_lst=[int(val==b.get(field)) for b in dataset]
        bitmap[val]=cur_lst
    return bitmap

def search(field,value):
    if(field not in bitmap_collection):
        bitmap=generate_bit_map(field)
        bitmap_collection[field]=bitmap
    if(not bitmap_collection.get(field).get(value)):
        return []
    search_result=[]
    for i in range(len(dataset)):
        if(not bitmap_collection.get(field).get(value)):
            return []
        if(bitmap_collection.get(field).get(value)[i]):
            search_result.append(dataset[i])
    return search_result

def and_search(field1,value1,field2,value2):
    if(field1 not in bitmap_collection):
        bitmap=generate_bit_map(field1)
        bitmap_collection[field1]=bitmap
    if(field2 not in bitmap_collection):
        bitmap=generate_bit_map(field2)
        bitmap_collection[field2]=bitmap
    if(not bitmap_collection.get(field1).get(value1)):
        return []
    if(not bitmap_collection.get(field2).get(value2)):
        return []
    search_result=[]
    for i in range(len(dataset)):
        if(bitmap_collection.get(field1).get(value1)[i] and bitmap_collection.get(field2).get(value2)[i]):
            search_result.append(dataset[i])
    return search_result

def or_search(field1,value1,field2,value2):
    if(field1 not in bitmap_collection):
        bitmap=generate_bit_map(field1)
        bitmap_collection[field1]=bitmap
    if(field2 not in bitmap_collection):
        bitmap=generate_bit_map(field2)
        bitmap_collection[field2]=bitmap
    if(not bitmap_collection.get(field1).get(value1) and not bitmap_collection.get(field2).get(value2)):
        return []
    if(not bitmap_collection.get(field1).get(value1)):
        return search(field2,value2)
    if(not bitmap_collection.get(field2).get(value2)):
        return search(field1,value1)
    search_result=[]
    for i in range(len(dataset)):
        if(bitmap_collection.get(field1).get(value1)[i] or bitmap_collection.get(field2).get(value2)[i]):
            search_result.append(dataset[i])
    return search_result


def main():
    print("Search gender='F':")
    for row in search("gender", "F"):
        print(row)
    print("-" * 40)

    print("\nSearch device_type='mobile':")
    for row in search("device_type", "mobile"):
        print(row)
    print("-" * 40)

    print("\nSearch region='Asia':")
    for row in search("region", "Asia"):
        print(row)
    print("-" * 40)

    print("\nAND Search: gender='F' AND region='EU'")
    for row in and_search("gender", "F", "region", "EU"):
        print(row)
    print("-" * 40)

    print("\nAND Search: gender='M' AND device_type='mobile'")
    for row in and_search("gender", "M", "device_type", "mobile"):
        print(row)
    print("-" * 40)

    print("\nAND Search: gender='F' AND device_type='desktop'")
    for row in and_search("gender", "F", "device_type", "desktop"):
        print(row)
    print("-" * 40)

    print("\nOR Search: gender='F' OR region='Africa'")
    for row in or_search("gender", "F", "region", "Africa"):
        print(row)
    print("-" * 40)

    print("\nOR Search: device_type='tablet' OR region='US'")
    for row in or_search("device_type", "tablet", "region", "US"):
        print(row)
    print("-" * 40)

    print("\nOR Search: gender='Other' OR region='Oceania' (Expected: empty result)")
    for row in or_search("gender", "Other", "region", "Oceania"):
        print(row)
    print("-" * 40)


if __name__=='__main__':
    main()


    




