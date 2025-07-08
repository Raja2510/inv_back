from fastapi import FastAPI
from supabase import create_client

database_url="https://zxcinfaprezgvhgvnwyh.supabase.co"
database_api="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp4Y2luZmFwcmV6Z3ZoZ3Zud3loIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxOTEyNzIsImV4cCI6MjA2NTc2NzI3Mn0.iEBk5TxKoIh7cPdJOb_cNyDCFyOcYwG9qUmDdFqRa2E"

database=create_client(supabase_url=database_url,supabase_key=database_api)

app =FastAPI()

# --------------supplier---------------------------------------------

@app.get("/supplier")
def get_supplier():
    result = database.table("supplier").select('*').execute()
    return result.data


@app.post("/supplier/create")
def create_supplier(name,age,contact):
    valid=database.table("supplier").select('*').eq("supplier_name",name).execute()
    if len(valid.data)==0:
        new_entry=database.table('supplier').insert(
            {
                'supplier_name':name,
                'supplier_age':age,
                'contact_info':contact
            }
        ).execute()
        return new_entry.data
    else:
        return "This person already exsist"

@app.put("/supplier/update")
def update_supplier(name,uname,age,contact):
    get_supplier=database.table("supplier").select("*").eq("supplier_name",name).execute()
    if get_supplier.data==[]:
        return  "This ID Doesnt Exsists"
    else:
        updated_supplier=database.table("supplier").update(
            {"supplier_name":uname,
             "supplier_age":age,
             "contact_info":contact
             }
        ).eq("supplier_name",name).execute()
        return updated_supplier.data
@app.delete("/supplier")
def delete_supplier(name):
    del_supplier=database.table("supplier").delete().eq("supplier_name",name).execute()
    if del_supplier.data==[]:
        return  "This ID Doesnt Exsists"
    else:
        return del_supplier.data
    








#------------------categories---------------------


@app.get("/category")
def get_categoryr():
    result = database.table("category").select('*').execute()
    return result.data

@app.post("/category/create")
def create_category(name,desc):
    valid=database.table("category").select('*').eq("category_name",name).execute()
    if len(valid.data)==0:
        new_entry=database.table('category').insert(
            {
                'category_name':name,
                'descreption':desc
                
            }
        ).execute()
        return new_entry.data
    else:
        return "This person already exsist"
    

#-------------PRODUCT---BACKEND-----------------
@app.post("/product/create")
def create_product(name,quantity,categoty,supplier):
    check=database.table("products").select("product_name").eq("product_name",name).execute()
    if check.data==[]:
        created_product=database.table("products").insert({
            "product_name":name,
            "quantity":quantity,
            "category":categoty,
            "supplier":supplier

    }).execute()
    else:
        return "this already esxist"
    return created_product.data

@app.get("/products")
def get_products():
    got_products=database.table("products").select("*").execute()
    return got_products.data
@app.put("/product/update")
def update_product(name,quantity,category,supplier):
    check=database.table("products").select("product_name").eq("product_name",name).execute()
    if check.data==[]:
        return "There is no such products"
    
    else:
        updated_product=database.table("products").update({
            "quantity":quantity,
            "category":category,
            "supplier":supplier
        }).eq("product_name",name).execute()
        return updated_product.data
@app.delete("/product/delete")
def delete_product(name):
    del_prosuct=database.table("products").delete().eq("product_name",name).execute()
    if del_prosuct.data==[]:
        return  "This ID Doesnt Exsists"
    else:
        return del_prosuct.data